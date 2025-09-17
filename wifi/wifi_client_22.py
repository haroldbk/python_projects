import socket
import time
import csv
import json 
import os

# Set up UDP client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.254.95', 12345)  # Adjust IP address and port as needed


    # Send request to the server
mycolor=input('please enter a value to start')
mycolor=mycolor.lower()
    
    #request_message = "16,18,19,17"
results = []  
filename = 'mydata.json'

if not os.path.exists(filename):
    with open(filename, 'w') as f:
        json.dump([],f)
#file_name= os.path.join(os.getcwd(),subfldr,filename)
client_socket.sendto(mycolor.encode(), server_address)
while True:  
    # Receive data from the server
    data, addr = client_socket.recvfrom(1024)
    print('Received data:', data.decode(), addr[0])
    rec = {"data": data.decode(), "from" : addr[0]}

    #load, append save back
    with open(filename,'r+') as f:
        content = json.load(f)
        content.append(rec)
        f.seek(0)
        json.dump(content, f, indent=4)
        f.truncate()
   
   