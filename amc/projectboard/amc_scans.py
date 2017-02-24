import sys, os
import subprocess


os.chdir('/root')
os.chdir("Projects")
os.chdir(sys.argv[1])
os.system('pwd')
os.system('ls')

os.system('pwd')
print ("............Scans.py..............")

l=int(sys.argv[2])
for i in range(1,l):
    com="sudo auto-multiple-choice getimages -debug /tmp/AMC-DEBUG-abc.log --progression-id analyse --copy-to  /root/Projects/"+ sys.argv[1]+"/scans/ --vector-density 300 --list list-file /root/Projects/"+ sys.argv[1]+"/scans/amc"+str(i)+".pdf"
    os.system(com)
