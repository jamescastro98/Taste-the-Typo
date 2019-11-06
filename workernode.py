from webbrowse import fetchURL
import socket
import time

s = socket.socket()

port = 330

s.settimeout(10)
s.connect(('127.0.0.1', port))

while True:
    server_msg = s.recv(1024)
    server_msg = server_msg.decode("utf-8")
    print(server_msg)
    s.send(bytes("message received!", encoding='utf-8'))
    # fetchURL(server_msg)  # commented out to test connection between nodes
    # send return value back to masternode?
    # grab next job
    s.close()
    s = socket.socket()
    s.connect(('127.0.0.1', port)) 
    # the way I (Joey) Edited it, I have the master node disconnect after receving data. this is to prevent timeouts
