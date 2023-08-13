#!/usr/bin/python3

import socket

IP_address = input("IP address: ")
port = int(input("Port: "))

client_socket = socket.socket()
client_socket.connect((IP_address, port))

answer = client_socket.recv(1024)
print(answer.decode("utf-8"))

client_socket.close()
