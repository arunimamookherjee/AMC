


with open("/root/Projects/out.json", "r") as myfile, open("out.json", "w") as out:
    data = myfile.readlines()
    print(data)
    for item in data:
        out.write(item)


print(data)