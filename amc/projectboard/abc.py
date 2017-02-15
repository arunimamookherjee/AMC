import os
from itertools import groupby
import json

os.system("pwd")
os.chdir("/root/Projects/")

names = ["name"]

with open("listmyfolder.txt", 'r') as f, open("out.json", "w") as out:
    out.write("{")
    for line in f:
        for word in line.split():
            out.write("{")
            out.write('"name" :')
            out.write('"' + word + '"')
            out.write("}")
    out.write("}")

f.close()

out.close()