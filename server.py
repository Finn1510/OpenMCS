import socket
import os
import struct
import pickle
from random import randint
from pygame import mixer



def init(port):
        fileBRAIN = []
        ourmusic = []        
        files = []
        musicPath = './music'
        
        #create music folder if non existent
        if os.path.exists(musicPath) == False :
                os.makedirs(musicPath)

        for entry in os.listdir(musicPath):
                if os.path.isfile(os.path.join(musicPath, entry)):
                        files.append(entry)
        
        s = socket.socket()
        host = socket.gethostname()
        s.bind((host,port))
        s.listen(5)
        print(host)
        print('waiting for any incoming conections ... ')

        conn,addr = s.accept()

        #get client identity
        ClientIPAddrBYTE = recv_msg(conn)
        ClientIPAddr = ClientIPAddrBYTE.decode('utf-8')

        if os.path.exists(ClientIPAddr) == True :
                print('client seen previously')

                #load client's song list
                fileBRAIN = pickle.load(open( ClientIPAddr, 'rb'))

                #compare files
                saveMusicList(ourmusic, musicPath)
                filesToTransmit = diff(ourmusic, fileBRAIN)

                #transmit new files client doesn't have
                transmitFiles(conn, filesToTransmit, fileBRAIN)

                #recieve music files we dont have
                receiveFiles(conn, fileBRAIN)

                #save client's song list
                pickle.dump(fileBRAIN, open(ClientIPAddr, 'wb'))

                #start playing music
                serverMainLoop(conn, ourmusic, musicPath)

        else: 
                print('client not seen previously')

                #transmit own music files to client
                transmitFiles(conn, files, fileBRAIN)
                
                #recieve music files we dont have
                receiveFiles(conn, fileBRAIN)

                #save client's song list
                pickle.dump(fileBRAIN, open(ClientIPAddr, 'wb'))

                #start playing music
                serverMainLoop(conn, ourmusic, musicPath)
                

def serverMainLoop(socket, ourmusic, musicPath):
        saveMusicList(ourmusic, musicPath)
        mixer.init()
        while True:
                randomsong = ourmusic[randint(0, (len(ourmusic) - 1 ))]
                randomsongBYTE = randomsong.encode('utf-8')
                send_msg(socket, randomsongBYTE)

                mixer.music.load('./music/' + randomsong)
                mixer.music.play()
                print('now playing: ' + randomsong)

                while mixer.music.get_busy() == True:
                    temp = 0
                else:
                        print('music ended picking next...')
                                      
def transmitFiles(socket, files, fileBRAIN):
        Transmissions = struct.pack('i',len(files))
        send_msg(socket, Transmissions) 
                
        for x in files:
                filename = str(x).encode('utf-8') 
                send_msg(socket, filename)

                file = open('./music/' + x , 'rb')
                file_data = file.read()
                send_msg(socket, file_data) 

                fileBRAIN.append(str(x))
                print(x + '\n' + 'has been send transmitted successfully')
                print('')

def receiveFiles(s, fileBRAIN):            
    i = 1

    transmissionsDATA = recv_msg(s) 
    transmissionsTUP = struct.unpack('i',transmissionsDATA)
    transmissions = transmissionsTUP[0]
    print('there are ' + str(transmissions) + ' awaiting receive transmissions')
    
    while i <= transmissions:
        BYTEfilename = recv_msg(s)
        filename = BYTEfilename.decode('utf-8')
        
        file = open('./music/' + filename, 'wb')
        file_data = recv_msg(s) 
        file.write(file_data)
        file.close()

        fileBRAIN.append(str(filename))
        print('transmission ' + str(i) + ' recieved')
        i = i + 1


def saveMusicList(musiclist, musicPath):
    for entry in os.listdir(musicPath):
                if os.path.isfile(os.path.join(musicPath, entry)):
                        musiclist.append(entry)

#find elements which are not in the other list
def diff(li1, li2): 
    return (list(set(li1) - set(li2)))                 


#TCP msg proctocoll

def send_msg(sock, msg):
    # Prefix each message with a 4-byte length (network byte order)
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)

def recv_msg(sock):
    # Read message length and unpack it into an integer
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    return recvall(sock, msglen)

def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data
