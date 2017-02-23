import os


os.system("cd")
os.system("pwd")
os.system("cd")
os.system("pwd")
f = open("/root/Project/listmyfolder.txt", 'r')

for word in f:

    print(word)
f.close()