import os
import sys

command1=" auto-multiple-choice prepare --with xelatex --filter plain --filtered-source /root/Projects/"+sys.argv[1]+"/DOC-filtered.tex  --out-sujet /root/Projects/"+sys.argv[1]+"/DOC-sujet.pdf --out-corrige /" \
         "root/Projects/"+sys.argv[1]+"/DOC-corrige.pdf --out-catalog /root/Projects/"+sys.argv[1]+"/DOC-catalog.pdf --out-calage /root/Projects/"+sys.argv[1]+"/DOC-calage.xy --mode s[sc] --n-copies "+ sys.argv[2]+\
         " /root/Projects/"+sys.argv[1]+"/source.txt --prefix /root/Projects/"+sys.argv[1]+"/ --latex-stdout"

os.system(command1)

#layout and

command4 = "auto-multiple-choice meptex  --src /root/Projects/" + sys.argv[1]
com1 = "/DOC-calage.xy --progression-id MEP --progression 1 --data /root/Projects/" +sys.argv[1] + "/data"
command4 += com1
os.system(command4)

