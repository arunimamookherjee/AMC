import sys, os
import subprocess


os.chdir('/root')
os.chdir("Projects")
os.chdir(sys.argv[1])
os.system('pwd')
os.system('ls')

command1="auto-multiple-choice export --data ./data \
  --module ods \
  --fich-noms students-list.csv \
  --o output-note.ods"

os.system(command1)
