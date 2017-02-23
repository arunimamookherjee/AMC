import sys, os
import subprocess


os.chdir('/root')
os.chdir("Projects")
os.chdir(sys.argv[1])
os.system('pwd')
os.system('ls')

command1="auto-multiple-choice association-auto --data ./data --notes-id numero-etudiant --liste ./students-list.csv --liste-key no"
os.system(command1)
