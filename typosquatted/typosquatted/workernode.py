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
    port = 6899
    s.settimeout(None)
    s.connect(('127.0.0.1', port)) # CHANGE TO 10.0.2.2 on VM!

    while True:
        server_msg = s.recv(1024)
        server_msg = server_msg.decode("utf-8")
        print(server_msg)
        filename = fetchURL(server_msg)  # commented out to test connection between nodes
        if(filename!="404"):
            s.send(bytes(filename+".html", encoding='utf-8'))
            sendFile(filename+".html", s)
            #time.sleep(1) # this should be uneccessary. if it leads to a problem we should have it sleep far less than 1 second
            
            s.send(bytes(filename+".png", encoding='utf-8'))
            sendFile(filename+".png", s)
            print('*** file sent')
            
        # send return value back to masternode?
        # grab next job
        s.close()
        s = socket.socket()
        s.connect(('127.0.0.1', port)) 
        # the way I (Joey) Edited it, I have the master node disconnect after receving data. this is to prevent timeouts

# if workernode.py is executed on its own
if __name__ == '__main__':
    start_worker()
