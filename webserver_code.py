
# UDPPingerServer.py
#generate randomized lost packets

import socket
import random 

# Create a UDP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
 
print('UDP server is listening...')
 
while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    # Capitalize the message from the client
    message = message.upper()
     # If rand is less than 4, the packet lost and do not respond
    if rand < 4:
        continue
    # Otherwise, the server responds
    serverSocket.sendto(message, address)

#client server
import time
import socket
 
 # creating a socket object for UDP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverName = ('localhost', 12000)  # server address and port number
clientSocket.settimeout(1)  #considers a packet loss after 1 sec



# 10 ping messages are sent to the serverPing
try:
    for i in range(10):
        stime = time.time()  # time when request is sent
        message = 'Reply from 127.0.0.1: ' + ' PING '  + str(i+1) + " " + time .ctime(stime) + '\n' # creates the message to send
        
        try:
            req = clientSocket.sendto(message.encode(),serverName)
            print('req' +'\n' + message)
            response, address = clientSocket.recvfrom(1024) # allows to recieve the data from server  
            print('response '+ response.decode()) # prints the data received from server
            endtime = time.time(); # current time
            roundt = endtime - stime #the round time
          
            print("RTT: " + str(roundt) + "sec" )

        except socket.timeout:
                print("\n"  + "Requested time out. " )

finally:
    print("socket connection ends")
    clientSocket.close()
            
