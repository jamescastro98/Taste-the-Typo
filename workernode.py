from webbrowse import fetchURL
import socket
import time
import json
import sys

def sendFile(filename, socket):
    try:
        f = open(filename, "rb")
        content = f.read(1024)
        while(content):
            socket.send(content)
            content=f.read(1024)
    except:
        print("No Result Found!")

running = True
def start_worker():
    global running
    s = None
    port = 6899
    f = open('workernodeConfig.json')
    config = json.load(f)
    f.close()
    ip = config["ip"]
    while running:
        while running:
            try:
                s = socket.socket()
                s.settimeout(None)
                s.connect((ip, port)) # CHANGE TO 10.0.2.2 on VM!
            except:
                print("unable to connect...")
                time.sleep(10)
                print("trying again.")
                continue
            break
        if not running:
            break
        server_msg = s.recv(1024)
        server_msg = server_msg.decode("utf-8")
        print(server_msg)
        filename = fetchURL(server_msg)  # commented out to test connection between nodes
        if(filename!="404"):
            s.send(bytes(filename + "~", encoding='utf-8'))
            sendFile(filename+".html", s)
            #time.sleep(1) #give it a second to process.
            
            #s.send(bytes(filename+".png", encoding='utf-8'))
            sendFile(filename+".png", s)
            print('*** file sent')
            
def kill(signalnumber, frame):
    global running
    running = False
# if workernode.py is executed on its own
if __name__ == '__main__':
    start_worker()
    signal.signal(signal.SIGINT, kill)
