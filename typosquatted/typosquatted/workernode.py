from .webbrowse import fetchURL
import socket
import time

def sendFile(filename, socket):
    try:
        f = open(filename, "rb")
        content = f.read(1024)
        while(content):
            socket.send(content)
            content=f.read(1024)
    except:
        print("No Result Found!")

def start_worker():
    s = socket.socket()
    port = 6789
    s.settimeout(10)
    s.connect(('127.0.0.1', port))

    while True:
        server_msg = s.recv(1024)
        server_msg = server_msg.decode("utf-8")
        print(server_msg)
        filename = fetchURL(server_msg)  # commented out to test connection between nodes
        s.send(bytes(filename, encoding='utf-8'))
        print('*** file sent')
        sendFile(filename, s)
        # send return value back to masternode?
        # grab next job
        s.close()
        s = socket.socket()
        s.connect(('127.0.0.1', port)) 
        # the way I (Joey) Edited it, I have the master node disconnect after receving data. this is to prevent timeouts

# if workernode.py is executed on its own
if __name__ == '__main__':
    start_worker()