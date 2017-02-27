import sys, os
import subprocess


os.chdir('/root')
os.chdir("Projects")
os.chdir(sys.argv[1])
os.system('pwd')
os.system('ls')

os.system('pwd')
print ("............Scans.py..............")




com1="sudo auto-multiple-choice prepare --mode b --prefix ./ ./test."+sys.argv[1]+" --data ./data/"
os.system(com1)


com2="sudo auto-multiple-choice meptex  --src /root/Projects/"+sys.argv[1]+"/DOC-calage.xy --progression-id MEP --progression 1 --data /root/Projects/"+sys.argv[1]+"/data"
os.system(com2)




l=int(sys.argv[2])
for i in range(1,l):
    com="sudo auto-multiple-choice getimages --progression-id analyse --copy-to  /root/Projects/"+ sys.argv[1]+"/scans/ --vector-density 300 --list list-file /root/Projects/"+ sys.argv[1]+"/scans/amc"+str(i)+".pdf"
    os.system(com)

com1="sudo auto-multiple-choice prepare --mode b --prefix ./ ./test.tex --data ./data/"
os.system(com1)

com2="sudo auto-multiple-choice prepare --n-copies 4 --with pdflatex" \
     " --filter latex --filtered-source /root/Projects/"+sys.argv[1]+"/DOC-filtered.tex --progression-id bareme --data /root/Projects/"+sys.argv[1]+"/data --mode b /root/Projects/"+sys.argv[1]+"/test.."+ sys.argv[1]
os.system(com2)

os.system("sudo auto-multiple-choice note --data ./data - --seuil 0.15 --grain 0.5 --arrondi s --notemin min --notemax max --no-plafond ")
st='""'
os.system(' sudo auto-multiple-choice note --data ./data --seuil 0.15 --grain 0.5 --arrondi inf --notemax 20 --plafond --notemin '+st+' --postcorrect-student '+st+' --postcorrect-copy '+st+' --progression-id notation --progression 1')







