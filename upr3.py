import sys
import os

for arg in sys.argv[1:]:
    current = open(arg, r)
    line = f.readline()
    while line:
      print (line)
      line = current.readline()
      print (line)
