from socket import *
from fib import fib

def fib_server(address):  # address is a tuple of IP and port number
    sock = socket(AF_INET, SOCK_STREAM)           # IPV4, TCP
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 
    sock.bind(address) # bind (reserve) the address for this socket
    sock.listen(5)  # sets the maximum number of sockets waiting for a connection (in a queue) to 5
    while True:
        client, addr = sock.accept()
        print("Connection", addr) # note how many times this is displayed!
        fib_handler(client)
        
def fib_handler(client):
    while True:
        req = client.recv(100) # read 100 bytes from the client
        if not req:
            break
        n = int(req)
        result = fib(n)
        resp = str(result).encode('ascii') + b'\n'
        client.send(resp)
    print("Closed")
    
print("Will now attempt to start listening at localhost:25000")
print("you may telnet or netcat (nc) to this host")

fib_server(('', 25000))

print("Server stopped")