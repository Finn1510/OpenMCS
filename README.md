# OpenMCS
<img src="https://github.com/Finn1510/OpenMCS/raw/master/Open%20MCS%20Logo.png" width="20%">

An Open Source tool to listen to music together with friends.
OpenMCS is short for Open music synchronizer. 
It synchronizes your music libruary with the libruary of your friend.
Just put your mp3 files in the music folder, connect to your friend or let your friend connect to you 
and enjoy listening to music together.
This is an Open source project and it will evolve over time. 
If you want to add or fix something don't mind to create a pull request. 

Also if you encounter any issues feel free to submit them on the Issues tab.

### Features

+ syncs your music libruary with the music libruary of your friend  
+ remembers music libruary from users (so it doesn't send the same mp3 files multiple times) 
+ plays music synced

### Planed Features

+ proper GUI 
+ support for more than 2 users 
+ automatic port forward solution 
+ friend system so you dont have to type in the IP every time

### Dependencies 

+ socket
+ struct      
+ pickle   
+ os         
+ pygame      (for audio playback)

### for Developers 
This is written and tested in Python 3.8 64bit it should work with all python 3.x versions tho. 

OpenMCS per default uses the port 5050.
The Programm structure should look like something like this:
<img src="https://github.com/Finn1510/OpenMCS/raw/master/archetecture.png" width="100%">
