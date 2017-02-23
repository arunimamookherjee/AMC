import sys, os
import subprocess


for i in range(10):
    print("*")

os.chdir("/root")
os.system('pwd')
os.system('ls')
os.chdir("Projects")
os.system('pwd')
print ("............Creating Project..............")

subprocess.Popen(["bash", "new_project.sh", sys.argv[1]])

print ("............Project Sucessfully Created................")
os.system('pwd')
os.system('ls')
