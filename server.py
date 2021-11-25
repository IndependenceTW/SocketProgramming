import socket
import threading


BUFFERLENGTH = 1024
SERVERIP = "127.0.0.1"
SERVERPORT = 48763
ADDR = (SERVERIP, SERVERPORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADDR)


def handle_client(conn, addr):
    print(f"[SERVER MSG] {addr} connected successful")
    connected = True

    while connected:
        msg = conn.recv(BUFFERLENGTH).decode(FORMAT)
        if(msg == DISCONNECT_MESSAGE):
            connected = False
        print(f"[FROM {addr}] {msg}")
        conn.send(("GET Your Message: " + msg ).encode(FORMAT))

    conn.close()
    print(f"[SERVER MSG] {addr} disconnected")
        


def start():
    try:
        print(f"[SERVER MSG] Server is listening on {SERVERIP}")
        server_socket.listen()
        while True:
            print("[SERVER MSG] Server is Waiting...")
            conn, addr = server_socket.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"[SERVER MSG] now active connections {threading.active_count() - 1}")
    except KeyboardInterrupt:
        print("[SERVER MSG] Bye")
        server_socket.close()

print("[SERVER MSG] Server is starting...")
start()
