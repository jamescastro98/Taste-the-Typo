from webbrowse import fetchURL
import socket
import time

socket = socket.socket()

port = 330

socket.settimeout(10)
socket.connect(('127.0.0.1', port))

while True:
    server_msg = socket.recv(1024)
    server_msg = server_msg.decode("utf-8")
    print(server_msg)
    socket.send(bytes("message received!", encoding='utf-8'))
    # fetchURL(server_msg)  # commented out to test connection between nodes
    # send return value back to masternode?
    # grab next job
    socket = socket.socket()
    socket.connect(('127.0.0.1', port)) 
    # the way I (Joey) Edited it, I have the master node disconnect after receving data. this is to prevent timeouts
