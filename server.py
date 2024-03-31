from socket import *
import time

serverPort = 8855

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', serverPort))
print('The server is ready to receive')

clients = {}

while True:
    data, address = sock.recvfrom(2048)
    message = data.decode()

    current_time = time.strftime('%H:%M:%S', time.localtime())

    print(f'Received message from {message} at {current_time}')

    clients[address] = (message, current_time)

    # Print the last received message from each client
    print("Server First name Last name")
    for index, (client_address, (client_message, client_time)) in enumerate(clients.items(), start=1):
        print(f"{index}- received message from {client_message} at {client_time}")

sock.close()
