import sys
import os

for arg in sys.argv[1:]:
	  input = open(arg, 'r')
	  A = input.readlines()
	  print(''.join(map(str, A)))