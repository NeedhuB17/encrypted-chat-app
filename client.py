import socket
from crypto import encrypt, decrypt

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    message = input("You: ")
    client.send(encrypt(message))

    data = client.recv(1024)
    reply = decrypt(data)
    print(reply)
