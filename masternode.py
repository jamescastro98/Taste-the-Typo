from typoGenerator import generateTypos
import socket
import sys


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

# server-side connection
socket = socket.socket()
port = 332
socket.bind(('', port))
socket.listen(5)

for typo in typos:
    msg = typo
    if typo.find("www.", 0, 4) != -1:
        msg = msg + ' = [valid]'   # debugging statement
        typo = typo.replace("www.","")
        if typo.find("https://", 0, 8)==-1:
            typo = 'https://'+typo
        # probably check if domain is also present
        print('Prepped '+typo+' to enter test()')   # debugging statement
        try:
            c, addr = socket.accept()
            c.send(bytes(typo, encoding='utf-8'))   # send typo to workernodes
                                                    # receive file from worker?
            c.close
        except:
            print('Error: unable to start thread')
    print(msg)  # debugging
