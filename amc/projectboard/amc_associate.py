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

os.system("sudo auto-multiple-choice prepare - --with pdflatex --filter latex --filtered-source ./DOC-filtered.tex --progression-id bareme --progression 1 --data  ./data --mode b ./test.tex")

l=int(sys.argv[2])
for i in range(1,l):
    com="sudo auto-multiple-choice getimages --progression-id analyse --copy-to  /root/Projects/"+ sys.argv[1]+"/scans/ --vector-density 300 --list list-file /root/Projects/"+ sys.argv[1]+"/scans/amc"+str(i)+".pdf"
    os.system(com)

os.system("sudo auto-multiple-choice analyse --projet ./ --data ./data --bw-threshold 0.6  --tol-marque 0.2 --liste-fichiers list.txt ")
os.system("sudo auto-multiple-choice note --data ./data - --seuil 0.15 --grain 0.5 --arrondi s --notemin min --notemax max --no-plafond ")
os.system("sudo auto-multiple-choice prepare - --with pdflatex --filter latex --filtered-source ./DOC-filtered.tex --progression-id bareme --progression 1 --data  ./data --mode b ./test.tex")
st='""'
os.system(' sudo auto-multiple-choice note --data ./data --seuil 0.15 --grain 0.5 --arrondi inf --notemax 20 --plafond --notemin '+st+' --postcorrect-student '+st+' --postcorrect-copy '+st+' --progression-id notation --progression 1')




os.system(" sudo auto-multiple-choice analyse --projet ./ ./scans/*")
os.system("sudo auto-multiple-choice note --data ./data --seuil 0.15")


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

