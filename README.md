# Black-Hat-Python
Python Programming for Hackers and Pentesters

## TCP_server.py
- Starts with passing in the IP address and port designated for the server to listen on.
- Next, telling the server to start listening, with maximum backlog of connections set to 5.
- The server is then put into a main loop, where it waits for an incoming connection.
- When a client connects, the client socket is received in the client variable and the remote connection details in the address variable.
- A thread object is then created that points to the `handle_client` function, pass it the client connection, at which point the main server loop is ready to handle another incoming connection.
- The `handle_client` fuction performs the recv() and then sends a simple message back to the client.
