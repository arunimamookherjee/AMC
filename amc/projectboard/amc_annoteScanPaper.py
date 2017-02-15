import sys, os
import subprocess


os.chdir('/root')
os.chdir("Projects")
os.chdir(sys.argv[1])
os.system('pwd')
os.system('ls')

command1= "auto-multiple-choice annote --projet ./ --data ./data --fich-noms students-list.csv"
comman2=" auto-multiple-choice regroupe --projet ./ --sujet DOC-subject.pdf --fich-noms students-list.csv --tex-src test.tex --compose0"


os.system(command1)
