import socket

BUFFERLENGTH = 2048
SERVERIP = "127.0.0.1"
SERVERPORT = 48763
ADDR = (SERVERIP, SERVERPORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)

def send(msg):
    client_socket.send(msg)
    print(client_socket.recv(BUFFERLENGTH).decode(FORMAT))

connected = True
while connected:
    msg = input("[To Server]: ")
    send(msg.encode(FORMAT))
    if(msg == DISCONNECT_MESSAGE):
        connected = False

client_socket.close()
