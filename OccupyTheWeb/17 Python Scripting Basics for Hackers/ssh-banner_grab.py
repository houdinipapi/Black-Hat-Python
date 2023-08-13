#!/usr/bin/python3

import socket

s = socket.socket()

host_name = input("IP address: ")

host = socket.gethostbyname(host_name)

port = 6996

s.connect((host, port))

answer = s.recv(1024)

print(answer.decode("ascii"))

s.close()
