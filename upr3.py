import sys
import os

for arg in sys.argv[1:]:
    file = open(arg, r)
    line = file.readline()
    while line:
        print (line)
        line = file.readline()
