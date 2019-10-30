from typoGenerator import generateTypos
from webbrowse import browse_helper
import sys
import os
import subprocess

typos = generateTypos('www.google.com')
print(typos)
    # for typo in typos:
    #     browse_helper(typo)
