# OpenMCS
<img src="https://github.com/Finn1510/OpenMCS/raw/master/Open%20MCS%20Logo.png" width="20%">

<iframe width="560" height="315" src="https://www.youtube.com/embed/VOEOaKkWJEo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

An Open Source tool to listen to music together with friends.
OpenMCS is short for Open music synchronizer. 
It synchronizes your music libruary with the libruary of your friend.
Just put your mp3 files in the music folder, connect to your friend or let your friend connect to you 
and enjoy listening to music together.
This is an Open source project and it will evolve over time. 
If you want to add or fix something don't mind to create a pull request. 

Also if you encounter any issues feel free to submit them on the Issues tab.

<h2 align="center"><a href="https://github.com/Finn1510/OpenMCS/releases" target="_blank"><b>Download latest Version</b></a></h2>

### Features

+ syncs your music libruary with the music libruary of your friend  
+ remembers music libruary from users (so it doesn't send the same mp3 files multiple times) 
+ plays music synced between server and client 
+ automatic port forward solution (UPNP)

### Planed Features

+ support for more than 2 users 
+ friend system so you dont have to type in the IP every time

### Dependencies 

+ socket
+ struct      
+ pickle   
+ os 
+ miniupnpc   
+ pygame      (for audio playback)

### for Developers 
This is written and tested in Python 3.7 32bit it should work with all python 3.x versions tho. 

OpenMCS per default uses the port 5050.
The Programm structure should look like something like this:
<img src="https://github.com/Finn1510/OpenMCS/raw/master/archetecture.png" width="100%">
