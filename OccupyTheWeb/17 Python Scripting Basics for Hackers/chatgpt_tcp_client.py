#!/usr/bin/python3

import socket


def scan_ports(target_host, port_list):
    for port in port_list:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(1)  # Set a timeout for the connection attempt

        try:
            client.connect((target_host, port))
            print(f"Port {port} is open")
            answer = client.recv(1024)
            print(answer.decode("ascii"))
        except (socket.timeout, ConnectionRefusedError) as e:
            # print(f"Port {port} is closed")
            print(e)
        finally:
            client.close()


if __name__ == "__main__":
    target_host = "172.31.0.1"  # Change this to the target IP address
    ports_to_scan = [21, 22, 25, 80, 443, 444, 3306]  # List of ports to scan

    scan_ports(target_host, ports_to_scan)
