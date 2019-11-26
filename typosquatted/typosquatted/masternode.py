from .typoGenerator import generateTypos
import socket as sock
import sys
import os
import threading
import signal
import time

# adjusts output from typoGenerator.py by:
#   removing "www." from the string (not sure if needed but is cleaner)
#   appending "https://" to the typo (webbrowse.py doesn't work otherwise)
def preptypo(typo):
    typo = typo.replace("www.","")
    if typo.find("https://", 0, 8)==-1: # checks if https:// is present so it doesn't double dip
        typo = 'https://'+typo
    print('Prepped '+typo+' to enter test()')   # debugging statement
    return typo

def recvfile(filename, addr):
    print("I genuinely don't know what this is supposed to do.")
    #f = open("MASTER"+filename,'wb')
    #content = addr.recv(1024)
    #while(content):
     #   f.write(content)
      #  content=addr.recv(1024)
    #f.close()

# sends tasks to workernode and then waits for work
def task_management(typo, addr):
    msg = bytes(typo, encoding='utf-8')
    addr.send(msg)   # send typo to workernodes
    filename = addr.recv(1024)               # this might not recv all of the data
    filename = filename.decode('utf-8')
    print("*** \""+filename+"\" recieved from worker")   # debugging
    recvfile(filename, addr)
    addr.close() # now I am expecting the worker node to re establish the connection

#arg = "messenger.com"  
# set arguments
#if len(sys.argv) < 2:
#    print("[Alert] no website specified.")
#    print("default value, \"" + arg + "\" set...") # debugging
#else:
#    arg = sys.argv[1]

#print("Will now generate typos for \"" + arg + "\" ") # debugging
# generate typos
#typos = generateTypos(arg)

#THIS IS WHAT JAMES ADDED
#os.mkdir(arg)
#os.mkdir((arg+'/HTML'))
#os.mkdir((arg+'/IMG'))
#THIS IS WHAT JAMES ADDED

# server-side connection

connections = []
socket = []
threads = []
running = True
def handleNewConnections():
    global connections
    global socket
    while True:
        (connection, addr) = socket.accept()
        connections.append([connection, addr])
        print(connections)

def shutdown(sig, frame):
    global threads
    global socket
    global running
    running = False
    print("shuting down...")
    for t in threads:
        t.join()
    socket.close()
    sys.exit(0)

def cleanup():
    global threads
    while True:
        time.sleep(2)
        for t in threads:
            if not t.isAlive():
                t.join()
                threads = [tr for tr in threads if not tr == t]
                print(t)
                print(threads)

def setupConnections():
    global socket
    socket = sock.socket()
    port = 6899
    socket.bind(('', port))
    socket.listen(5)

    connectionsThread = threading.Thread(target = handleNewConnections, args = ())
    connectionsThread.setDaemon(True)
    connectionsThread.start()
    cleanupThread = threading.Thread(target = cleanup, args = ())
    cleanupThread.setDaemon(True)
    cleanupThread.start()


def gatherTypoSquatSites(arg="google.com"):
    global connections
    global threads
    global running
    responces = 0
    typos = generateTypos(arg)
    totaltypos = len(typos)
    for typo in typos:
        msg = typo
        if typo.find("www.", 0, 4) != -1:
            msg = msg + ' = [valid]'   # debugging statement
            typo = preptypo(typo)       # refer to preptypo() 
            # probably check if domain is also present
            try:
                while len(connections) == 0 and running == True: #stop untill a new connection comes through or the program terminates
                    pass
                if running == False:
                    return
                (con, ad) = connections[0]
                connections = connections[1:]
                cur_thread = threading.Thread(target=task_management, args=(typo, con))
                threads.append(cur_thread)
                cur_thread.start()
                # task_management(typo, c)   # for threadless testing
            except:
                print('Error: unable to start thread')
        # print(msg)  # debugging
