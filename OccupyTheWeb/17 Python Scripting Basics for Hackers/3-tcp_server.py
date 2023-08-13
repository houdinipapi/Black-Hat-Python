#!/usr/bin/python3

import socket

TCP_IP = input("IP address: ")
TCP_PORT = int(input("Port: "))
BUFFER_SIZE = 100

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((TCP_IP, TCP_PORT))
server_socket.listen(3)

conn, addr = server_socket.accept()
print("Connection address: ", addr)

while True:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
    print("Received data: ", data)
    conn.send(data)  #echo

conn.close()
