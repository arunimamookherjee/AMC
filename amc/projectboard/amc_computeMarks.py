import sys, os
import subprocess


os.chdir('/root')
os.chdir("Projects")
os.chdir(sys.argv[1])
os.system('pwd')
os.system('ls')

command1="auto-multiple-choice note --data ./data --seuil 0.15"
os.system(command1)
