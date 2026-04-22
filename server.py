import socket
import threading
from crypto import encrypt, decrypt

HOST = '0.0.0.0'
PORT = 5000

clients = []

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr}")
    clients.append(conn)

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break

            message = decrypt(data)
            print(f"{addr}: {message}")

            with open("chat.log", "a") as f:
                f.write(f"{addr}: {message}\n")

            for client in clients:
                if client != conn:
                    client.send(encrypt(f"{addr}: {message}"))

        except:
            break

    conn.close()
    clients.remove(conn)
    print(f"[DISCONNECTED] {addr}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server running...")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
