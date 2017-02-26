import sys, os
import subprocess


os.chdir('/root')
os.chdir("Projects")
os.chdir(sys.argv[1])
os.system('pwd')
os.system('ls')

os.system('pwd')
print ("............check.py..............")

com1="sudo auto-multiple-choice prepare --mode b --prefix ./ ./test.tex --data ./data/"
os.system(com1)

com2="sudo auto-multiple-choice meptex  --src /root/Projects/"+sys.argv[1]+"/DOC-calage.xy --progression-id MEP --progression 1 --data /root/Projects/"+sys.argv[1]+"/data"
os.system(com2)

com3="sudo auto-multiple-choice note --data ./data --seuil 0.15"
os.system(com3)

com4="sudo  auto-multiple-choice annote --projet ./ --data ./data --fich-noms students-list.csv"
os.system(com4)

com5="sudo auto-multiple-choice export --data ./data \
  --module ods \
  --fich-noms students-list.csv \
  --o output-note.ods"
os.system(com5)