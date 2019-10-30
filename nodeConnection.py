from typoGenerator import generateTypos
from webbrowse import test
import sys
import _thread

typos = generateTypos('https://amazon.com')
print(typos)
for typo in typos:
    try:
        _thread.start_new_thread(test(typo))
    except:
        print('Error: unable to start thread')