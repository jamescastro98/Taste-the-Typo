from .typoGenerator import generateTypos
import socket as sock
import sys
import os
import threading
import signal
import time

globalInput =  ""

# adjusts output from typoGenerator.py by:
#   removing "www." from the string (not sure if needed but is cleaner)
#   appending "https://" to the typo (webbrowse.py doesn't work otherwise)
def preptypo(typo):
    typo = typo.replace("www.","")
    if typo.find("https://", 0, 8)==-1: # checks if https:// is present so it doesn't double dip
        typo = 'https://'+typo
    # print('Prepped '+typo+' to enter test()')   # debugging statement: successful prep
    return typo

def recvfile(filename, addr):
    # print("I genuinely don't know what this is supposed to do.")
    content = addr.recv(1024)
    store=content
    while(content):
        content=addr.recv(1024)
        store+=content
    htmldelim=bytearray('</html>','utf-8')
    pngdelim=bytearray('.png','utf-8')
    try:
        bytarr=store.split(htmldelim,1)
        htmldoc=bytarr[0].decode('utf-8')
        #htmldoc+="</html>"
        rest=bytarr[1]
        pngarr=rest.split(pngdelim,1)
        pngname=pngarr[0].decode('utf-8')
        f = open("./data/" + globalInput + "/" + filename,'wb')
        htmldoc=htmldoc+"</html>"
        print(htmldoc)
        f.write(htmldoc.encode('utf-8'))
        f.close()
        #print(str(pngarr[1]))
        print(pngname +".png")
        x=open("./data/" + globalInput + "/"+(pngname+".png"),'wb')
        x.write(pngarr[1])
        x.close()
    except:
        amcry=1
 

# sends tasks to workernode(s) and then waits for work
def task_management(typo, addr):
    msg = bytes(typo, encoding='utf-8')
    addr.send(msg)   # send typo to workernodes
    filename = addr.recv(1024)               # this might not recv all of the data
    filename = filename.decode('utf-8')
    print("*** \""+filename+"\" recieved from worker")   # debugging: successful retrieval
    if(filename!="404"):
        recvfile(filename, addr)
    addr.close() # now I am expecting the worker node to re establish the connection

# server-side connection

connections = []
socket = []
threads = []
running = True
# accepts new connections from workernode.py
def handleNewConnections():
    global connections
    global socket
    while True:
        (connection, addr) = socket.accept()
        connections.append([connection, addr])
        # print(connections)    # debugging

# closes all threads and then ends program
def shutdown(sig, frame):
    global threads
    global socket
    global running
    running = False
    # print("shutting down...")  # debugging: about to enter shutdown
    for t in threads:
        t.join()
    socket.close()
    sys.exit(0)

# cleans up all threads
def cleanup():
    global threads
    while True:
        time.sleep(2)
        for t in threads:
            if not t.isAlive():
                t.join()
                threads = [tr for tr in threads if not tr == t]
                # print(t)  # debugging
                # print(threads)    # debugging

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

# creates a task for each typo that a workernode (workernode.py) can pick up and retrieve the site for
def gatherTypoSquatSites(arg="google.com"):
    global connections
    global threads
    global running

    global globalInput
    globalInput = arg
    if not os.path.isdir('./data/{}'.format(arg)):
      os.makedirs('./data/{}'.format(arg))
      siteTracker=open("index.txt",'a')
      siteTracker.write(arg)
      siteTracker.close
    # responces = 0
    typos = generateTypos(arg)
    # totaltypos = len(typos)
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
