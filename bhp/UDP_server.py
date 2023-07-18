import socket

host = "127.0.0.1"
port = 9997

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the host and port
server_socket.bind((host, port))
print(f"UDP server listening on {host}:{port}")

while True:
    # Receive data and the address of the client
    data, addr = server_socket.recvfrom(4096)
    print("Received:", data.decode())
    print("From:", addr)

    # Send a response back to the client
    response = "Blah blah blah"
    server_socket.sendto(response.encode(), addr)
