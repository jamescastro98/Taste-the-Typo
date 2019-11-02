from webbrowse import fetchURL
import socket
import time

socket = socket.socket()

port = 332

socket.connect(('127.0.0.1', port))
socket.settimeout(10)

while True:
    server_msg = socket.recv(1024)
    server_msg = server_msg.decode("utf-8")
    print(server_msg)
    fetchURL(server_msg)  
    # send return value back to masternode?
    # grab next job
