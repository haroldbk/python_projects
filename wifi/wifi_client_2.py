import socket
import time

# Set up UDP client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.254.95', 12345)  # Adjust IP address and port as needed
pattern = []
for i in range(1, 5):
    order = input('enter a number between 16 and 19:')
    pattern.append(order)

print('Pattern:', pattern)
strPattern=pattern[0] +','+ pattern[1]+',' + pattern[2]+',' + pattern[3]
print('Pattern as string:', strPattern)



while True:
    # Send request to the server
    #request_message = "SEND DATA"
    request_message = strPattern
    client_socket.sendto(request_message.encode(), server_address)
    
    # Receive data from the server
    data, addr = client_socket.recvfrom(1024)
    print('Received data:', data.decode())
    
    # Send acknowledgment back to server
    #ack_message = "Data received successfully"
    #client_socket.sendto(ack_message.encode(), addr)
    
    # Wait for 10 seconds before next request
    time.sleep(10)