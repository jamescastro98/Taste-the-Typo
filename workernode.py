from webbrowse import fetchURL
import socket
import time

socket = socket.socket()

port = 330

socket.settimeout(10)
socket.connect(('127.0.0.1', port))

i = 0
while i < 3:
    server_msg = socket.recv(1024)
    server_msg = server_msg.decode("utf-8")
    print(server_msg)
    socket.send(bytes("message received!", encoding='utf-8'))
    i = i + 1

# while True:
    # fetchURL(server_msg)  # commented out to test connection between nodes
    # send return value back to masternode?
    # grab next job
