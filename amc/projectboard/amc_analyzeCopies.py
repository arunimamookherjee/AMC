import sys, os
import subprocess


os.chdir('/root')
os.chdir("Projects")
os.chdir(sys.argv[1])
os.system('pwd')
os.system('ls')
##analyse
command1="sudo auto-multiple-choice analyse --debug /tmp/AMC-DEBUG-F6GpP7FN.log --multiple --tol-marque 0.2,0.2 --prop 0.8 --bw-threshold 0.6 --progression-id analyse" \
         " --progression 1 --n-procs 0 --data /root/Projects/"+sys.argv[1]+"/data --projet /root/Projects/hello7.0/ --cr /root/Projects/"+sys.argv[1]+"/cr --liste-fichiers /tmp/liste-jgt4RW --no-ignore-red"
os.system(command1)
##marking
command2="sudo auto-multiple-choice note --debug /tmp/AMC-DEBUG-F6GpP7FN.log --data /root/Projects/"+sys.argv[1]+"/data --seuil 0.15 --grain 0.5 --arrondi inf --notemax 20 --plafond --notemin  --postcorrect-student  --postcorrect-copy  --progression-id notation --progression 1"
os.system(command2)