#! /Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8

import sys

lnb = 0

n = 0 #number of bridgeports
m = 0 #number of bridges

for line in sys.stdin:
    # print(line,end="")
    print(lnb)
    if lnb == 0:
        
    lnb = lnb + 1