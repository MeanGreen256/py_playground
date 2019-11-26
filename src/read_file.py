import re
import sys
import subprocess

file_name = sys.argv[1]

with open(file_name) as f:
   alist = f.read().splitlines() 


for item in alist:
   print "docker save" + item + "-o" + item
   cmd = "docker save " + item + " -o " + item
   returned_value = subprocess.call(cmd,shell=True)
   print('returned value:', returned_value)
