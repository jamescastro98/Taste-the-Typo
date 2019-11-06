from typoGenerator import generateTypos
import socket
import sys
import os
import threading

# adjusts output from typoGenerator.py by:
#   removing "www." from the string (not sure if needed but is cleaner)
#   appending "https://" to the typo (webbrowse.py doesn't work otherwise)
def preptypo(typo):
    typo = typo.replace("www.","")
    if typo.find("https://", 0, 8)==-1: # checks if https:// is present so it doesn't double dip
        typo = 'https://'+typo
    print('Prepped '+typo+' to enter test()')   # debugging statement
    return typo

# sends tasks to workernode and then waits for work
def task_management(typo, addr):
    msg = bytes(typo, encoding='utf-8')
    addr.send(msg)   # send typo to workernodes
    worker_msg = addr.recv(1024)               # this might not recv all of the data
    worker_msg = worker_msg.decode("utf-8")
    print('******************************************')
    print(worker_msg)   # debugging
    print('******************************************')
    addr.close() # now I am expecting the worker node to re establish the connection

arg = "messenger.com"  
# set arguments
if len(sys.argv) < 2:
    print("[Alert] no website specified.")
    print("default value, \"" + arg + "\" set...") # debugging
else:
    arg = sys.argv[1]

print("Will now generate typos for \"" + arg + "\" ") # debugging
# generate typos
typos = generateTypos(arg)

#THIS IS WHAT JAMES ADDED
#os.mkdir(arg)
#os.mkdir((arg+'/HTML'))
#os.mkdir((arg+'/IMG'))
#THIS IS WHAT JAMES ADDED

# server-side connection

connections = []

socket = socket.socket()
port = 330
socket.bind(('', port))
socket.listen(5)

def handleNewConnections():
    global connections
    while True:
        (connection, addr) = socket.accept()
        connections.append([connection, addr])

connectionsThread = threading.Thread(target = handleNewConnections, args = ())
connectionsThread.setDaemon(True)
connectionsThread.start()

for typo in typos:
    msg = typo
    if typo.find("www.", 0, 4) != -1:
        msg = msg + ' = [valid]'   # debugging statement
        typo = preptypo(typo)       # refer to preptypo() 
        # probably check if domain is also present
        try:
            while (len(connections) == 0):
                pass
                # halt until new connection comes through
            (con, ad) = connections.pop(1)
            print(con,ad)
            cur_thread = threading.Thread(target=task_management, args=(typo, con))
            cur_thread.start()
            # task_management(typo, c)   # for threadless testing
        except:
            print('Error: unable to start thread')
    # print(msg)  # debugging
