import sys, os
import subprocess


os.chdir('/root')
os.chdir("Projects")
os.chdir(sys.argv[1])
os.system('pwd')
os.system('ls')


command="sudo auto-multiple-choice prepare --with xelatex --filter plain --filtered-source /root/Projects/"+sys.argv[1]+"/DOC-filtered.tex " \
        " --out-sujet /root/Projects/"+sys.argv[1]+"/DOC-sujet.pdf --out-corrige /root/Projects/"+sys.argv[1]+"/DOC-corrige.pdf " \
        "--out-catalog /root/Projects/"+sys.argv[1]+"/DOC-catalog.pdf --out-calage /root/Projects/hello"+sys.argv[1]+"/DOC-calage.xy --mode s[sc] --n-copies 3 " \
        "/root/Projects/"+sys.argv[1]+"/source."+sys.argv[1]+" --prefix /root/Projects/"+sys.argv[1]+"/ --latex-stdout"

os.system(command)