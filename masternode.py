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
    worker_msg = addr.recv(1024)               # receive file from worker?
    worker_msg = worker_msg.decode("utf-8")
    print('******************************************')
    print(worker_msg)   # debugging
    print('******************************************')

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
socket = socket.socket()
port = 330
socket.bind(('', port))
socket.listen(5)
c, addr = socket.accept()
print("connected to ", addr)
i = 0
while i < 3:
    task_management("https://messenger.com", c)
    i = i + 1
# for typo in typos:
#     msg = typo
#     if typo.find("www.", 0, 4) != -1:
#         msg = msg + ' = [valid]'   # debugging statement
#         typo = preptypo(typo)       # refer to preptypo() 
#         # probably check if domain is also present
#         try:
#             # cur_thread = threading.Thread(target=task_management, args=(typo, socket))
#             # cur_thread.start()
#             task_management(typo, addr)   # for threadless testing
#         except:
#             print('Error: unable to start thread')
#     # print(msg)  # debugging
