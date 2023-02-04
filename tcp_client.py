"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket

HOST = "172.20.10.2" # Standard loopback interface address (localhost)
PORT = 6476 # Port to listen on

def main():
    # TODO: Create a socket and connect it to the server at the designated IP and port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
         # TODO: Get user input and send it to the server using your TCP socket
        message = input("Message: ")
        s.sendall(message.encode('utf-8'))
        data = s.recv(1024)
    
    # TODO: Receive a response from the server and close the TCP connection
    print(f"Received {data!r}")
    
    pass # Use the socket object without calling s.close().


if __name__ == '__main__':
    main()