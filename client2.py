import socket
import time

buffer_size = 1024
serverName = '192.168.1.15'
serverPort = 8855

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


first_name = "jenin"
last_name = "mansour"

while True:
    message = f'{first_name} {last_name}'
    sock.sendto(message.encode(), (serverName, serverPort))
    print(f'Sent message: {message}')
    time.sleep(2)

sock.close()
