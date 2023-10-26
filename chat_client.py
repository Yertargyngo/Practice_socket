import socket

socket_server = socket.socket()

from wsgiref.simple_server import server_version

name = input("Enter client name: ")
socket_server.connect(("127.0.0.1", 50))
socket_server.send(name.encode())
socket_name = socket_server.recv(1024)
server_name = socket_name.decode()
print(server_name, " connected!")

while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message)
    message = input("I: ")
    socket_server.send(message.encode())