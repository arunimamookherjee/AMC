import sys, os
import subprocess


os.chdir('/root')
os.chdir("Projects")
os.chdir(sys.argv[1])
os.system('pwd')
os.system('ls')

command1=" sudo auto-multiple-choice prepare --mode s --prefix ./ ./test.tex \
    --out-sujet DOC-subject.pdf \
    --out-corrige DOC-correction.pdf \
    --out-calage DOC-calage.xy"

os.system(command1)
os.system('ls')
os.system('pwd')

command2="sudo auto-multiple-choice prepare --mode b --prefix ./ ./test.tex --data ./data/"
os.system(command2)

command3="sudo auto-multiple-choice meptex --src /root/Projects/"+sys.argv[1]+"/DOC-calage.xy --data /root/Projects/"+sys.argv[1]+"/data"
os.system(command3)

command4 = "auto-multiple-choice meptex  --src /root/Projects/" + sys.argv[1]
com1 = "/DOC-calage.xy --progression-id MEP --progression 1 --data /root/Projects/" +sys.argv[1] + "/data"
command4 += com1
os.system(command4)
