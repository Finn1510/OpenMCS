import socket
import struct
import os
import pickle
from pygame import mixer


def connect(host, port):
    ourmusic = []
    fileBRAIN = []
    musicPath = './music'

    
    s = socket.socket()
    s.connect((host,port))
    print('conected to ',host)

    #identify self
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)    
    IPAddrBYTE = str(IPAddr).encode('utf-8')
    send_msg(s, IPAddrBYTE)

    if os.path.exists(str(host)) == True :
            print('server seen previously')

            #load host's song list
            fileBRAIN = pickle.load(open( str(host), 'rb'))

            #recieve new files from host
            receiveFiles(s, fileBRAIN)

            #compare files
            saveMusicList(ourmusic, musicPath)
            filesToTransmit = diff(ourmusic, fileBRAIN)

            #transmit music which host dont have
            transmitFiles(s , filesToTransmit, fileBRAIN)

            #save host's song list
            pickle.dump(fileBRAIN, open(str(host), 'wb'))

            #start playing music
            clientMainLoop(s)

    else: 
            print('server not seen previously')

            #recieve music files from host
            receiveFiles(s, fileBRAIN)

            #compare files
            saveMusicList(ourmusic, musicPath)
            filesToTransmit = diff(ourmusic, fileBRAIN)

            #transmit music which host dont have
            transmitFiles(s , filesToTransmit, fileBRAIN)

            #save host's song list
            pickle.dump(fileBRAIN, open(str(host), 'wb'))

            #start playing music
            clientMainLoop(s)

def clientMainLoop(socket):
    mixer.init()
    while True:
        randomsongBYTE = recv_msg(socket)
        randomsong = randomsongBYTE.decode('utf-8')
        
       
        mixer.music.load('./music/' + randomsong)
        mixer.music.play()
        print('now playing: ' + randomsong)
        
        while mixer.music.get_busy() == True:
            temp = 0
        else:
            print('music ended receiving next...')

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
    print('there are ' + str(transmissions) + ' awaiting  receive transmissions')
    
    while i <= transmissions:
        BYTEfilename = recv_msg(s)
        filename = BYTEfilename.decode('utf-8')
        
        file = open('./music/' + filename, 'wb')
        file_data = recv_msg(s) 
        file.write(file_data)
        file.close()

        fileBRAIN.append(str(filename))
        print('transmission ' + str(i) + ' recieived')
        i = i + 1

    
def saveMusicList(musiclist, musicPath):
    for entry in os.listdir(musicPath):
                if os.path.isfile(os.path.join(musicPath, entry)):
                        musiclist.append(entry)

#find elements which are not in the other list                        
def diff(li1, li2): 
    return (list(set(li1) - set(li2)))         

#TCP msg protocoll

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

 
