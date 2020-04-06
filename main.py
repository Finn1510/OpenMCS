import pickle
import os

import server
import client

choice = int(input('HOST (1) or CONNECT (2) (1/2)>>>'))

if choice == 1:
    print('starting server...')
    print('')
    server.init(5050)

elif choice == 2:
    IP = str(input('IP: >>>')) #25.122.134.57
    print('starting client...')
    print('')
    client.connect(IP,5050) 

else:
    print('Invalid Choice')


    





