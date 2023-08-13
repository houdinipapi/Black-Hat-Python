#!/usr/bin/python3

import socket

IP_address = "172.36.65.2"
port = 21

client_socket = socket.socket()
client_socket.connect((IP_address, port))

answer = client_socket.recv(1024)
print(answer)

client_socket.close()
