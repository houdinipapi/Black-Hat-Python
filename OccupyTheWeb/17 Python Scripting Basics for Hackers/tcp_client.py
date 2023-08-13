#!/usr/bin/python3

import socket

IP_address = input("IP address: ")
ports = [21, 22, 25, 3306]

for i in (0, 4):
    s = socket.socket()

    port = ports[i]

    print("This is the Banner for the Port")

    print(ports)

    s.connect((IP_address, port))

    answer = s.recv(1024)

    print(answer)

    s.close()
