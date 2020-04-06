import server
import client

import tkinter 
import tkinter.font as tkFont
import threading

#color pallet (from dark to bright) #0F2027 #203A43 #2C5364

root = tkinter.Tk()
t = tkinter.Label(root, text='OpenMCS',font='Helvetica 18 bold',fg = ('white'), bg = ('#2C5364'))
t.pack(fill = "x")

root.geometry('300x250')
root.configure(background='#0F2027')
root.title('Open MCS')
root.iconbitmap("icon.ico")

fontStyle = tkFont.Font(family="Lucida Grande", size=50)

def startServerThread():
    h.configure(state = 'disabled')
    c.configure(state = 'disabled')
    hLabel.place(x = 100, y = 200) 

    st = threading.Thread(target=startServer, args=(), daemon=True)
    st.start()

def startClientThread():
    h.configure(state = 'disabled')
    c.configure(state = 'disabled')
    cLabel.place(x = 90, y = 200) 
    
    IP = i.get()
    ct = threading.Thread(target=startClient, args=(IP,), daemon=True)
    ct.start()

def startServer():
    print('starting server...')
    print('')
    server.init(5050)

def startClient(IP):
    print('starting client...')
    print('')
    client.connect(IP,5050) 

h = tkinter.Button(root, text="Host", padx = 20, fg = ('white'),activeforeground = ('white') , bg = ('#203A43'), activebackground = ('#2C5364'), borderwidth = 0 , font = ('bold') , command=startServerThread)
h.place(x = 30 , y = 100)

c = tkinter.Button(root, text="Connect", padx = 20, fg = ('white'),activeforeground = ('white') , bg = ('#203A43'), activebackground = ('#2C5364'), borderwidth = 0 , font = ('bold') , command=startClientThread)
c.place(x = 150 , y = 100)

i = tkinter.Entry(root, width = 15, bg = ('#2C5364') , fg = ('#cfcfcf'), borderwidth = 0, font = ('bold') )    
i.place(x = 150 , y = 130)


hLabel = tkinter.Label(root, text = ('HOSTING...'), font = ('fontstyle'),fg = ('white'), bg = ('#0F2027'),)
cLabel = tkinter.Label(root, text = ('CONNECTED'), font = ('fontstyle'),fg = ('white'), bg = ('#0F2027'),)

root.mainloop()
