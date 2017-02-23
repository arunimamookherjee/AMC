import sys, os
import subprocess


os.chdir('/root')
os.chdir("Projects")
os.chdir(sys.argv[1])
os.system('pwd')
os.system('ls')
command1="auto-multiple-choice association --data ./data --list"

#command2="auto-multiple-choice association --data ./data --set --student 12 --id 3177"
#This would associate sheet 12 with student ID 3177.
os.system(command1)