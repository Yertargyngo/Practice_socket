import os
import socket
import webbrowser

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.1.116", 6954))
server.listen()

while True:
    user, adres = server.accept()

    while True:
        data = user.recv(1024).decode("utf-8").lower()
        print(data)

        #URL

        if data == "youtube":
            webbrowser.open("https://www.youtube.com/watch?v=rCHzZflWHZs")
            
        elif data == "whatsapp":
            webbrowser.open("https://web.whatsapp.com/")
        elif data == "jut-su":
            webbrowser.open("https://jut.su/")

        # Apps

        elif data == "pgadmin":
            os.startfile("C:/Program Files/PostgreSQL/15/pgAdmin 4/bin/pgAdmin4.exe")

        else:
            webbrowser.open("Missing it")


# print(socket.gethostbyname(socket.gethostname()))
# print()

