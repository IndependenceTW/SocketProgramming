import socket
import threading


BUFFERLENGTH = 1024
SERVERIP = "127.0.0.1"
SERVERPORT = 48763
ADDR = (SERVERIP, SERVERPORT)
FORMAT = 'utf-8'
RESPONSE_MSG = "HTTP/1.1 200 OK\r\n"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADDR)

def handle_request(msg):
    if(len(msg) == 0):
        return RESPONSE_MSG

    msg = msg.split()
    print(f"{msg[1]}")
    
    response_msg = RESPONSE_MSG + "Content-Type: text/html\r\n\r\n"
    print(response_msg)
    file = open("./pages/index.html")
    for line in file:
        response_msg += line
    file.close()
    print(response_msg)
    
    return response_msg

def handle_client(conn, addr):
    try:
        print(f"[SERVER MSG] {addr} connected successful")
        connected = True

        # while connected:
        req_msg = conn.recv(BUFFERLENGTH).decode(FORMAT)
        # if(msg == DISCONNECT_MESSAGE):
        #     connected = False
        print(f"[FROM {addr} request]\n {req_msg}")
        res_msg = handle_request(req_msg)
        conn.send(res_msg.encode(FORMAT))

        conn.close()
        print(f"[SERVER MSG] {addr} disconnected")
    except KeyboardInterrupt:
        print("Bye")
        return



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
        print("[SERVER MSG] Server Down")
        
        server_socket.close()
        exit(0)

print("[SERVER MSG] Server is starting...")
start()
