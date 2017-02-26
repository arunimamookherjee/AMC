import sys, os
import subprocess
import csv

os.chdir('/root')
os.chdir("Projects")
os.chdir(sys.argv[1])
os.system('pwd')
os.system('ls')

os.system('pwd')
print ("............Associate.py..............")



com3="sudo auto-multiple-choice note --data ./data --seuil 0.15"
os.system(com3)

os.system("auto-multiple-choice prepare  --with pdflatex --filter latex --filtered-source ./DOC-filtered.tex --progression-id bareme --data ./data --mode b ./test.tex")
os.system("auto-multiple-choice note  -- data ./data --seuil 0.15 --grain 0.5 --arrondi inf --notemax 20 --plafond --notemin "" --postcorrect-student "" --postcorrect-copy "" ")

os.system("auto-multiple-choice association --data ./data --list")
com3=" sudo auto-multiple-choice note  --data /root/Projects/new/data --seuil 0.15 --grain 0.5 --arrondi inf --notemax 20 --plafond --notemin "" --postcorrect-student "" --postcorrect-copy"
os.system(com3)

i=1
with open('/home/sony/Desktop/als.csv') as csvfile:
   reader = csv.DictReader(csvfile)
   for row in reader:
        print(row['name'])

        com="sudo auto-multiple-choice association --data ./data --set --student "+str(i)+" --id "+row['name']
        os.system(com)
        i+=1
        print("hua")


os.system("sudo auto-multiple-choice association --data ./data --list")


os.system("sudo auto-multiple-choice annote --projet ./ --data ./data --fich-noms students-list.csv")
os.system("sudo auto-multiple-choice regroupe --projet ./ --sujet DOC-subject.pdf --fich-noms students-list.csv --tex-src test.tex --compose")
os.system("sudo auto-multiple-choice export --data ./data \
  --module ods \
  --fich-noms students-list.csv \
  --o output-note.ods")

