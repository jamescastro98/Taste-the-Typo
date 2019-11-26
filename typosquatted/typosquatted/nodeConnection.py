from typoGenerator import generateTypos
from webbrowse import fetchURL
import sys
import _thread
import string

typos = generateTypos('messenger.com') # switch to sysargv for custom input
                                            # valid input: "https://amazon.com"
# print(typos)
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
            _thread.start_new_thread(fetchURL(typo))
        except:
            print('Error: unable to start thread')
    print(msg)  # debugging
    