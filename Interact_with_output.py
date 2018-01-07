#!/usr/bin/env python
#This script does ineteraction with script test.sh and gives first name and last name as inputs
try:
   import subprocess
   import os
   import sys
   import pdb
except Exception, e:
   print "Failed to import base modules: %s" %e
   sys.exit(3)
L=["Jawad\n","Hussain\n"]
sp=subprocess.Popen(["./test.sh"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=False)
for i in L:
   sp.stdin.write(i)
for line in sp.stdout.readlines():
   print line
#Following are the contents of test.sh
##!/usr/bin/env sh
#echo "Enter Your First Name: "
#read fname
#echo "Enter Your Last Name: "
#read lname
#echo "Your First Name: $fname"
#echo "Your Last Name: $lname"
