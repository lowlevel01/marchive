file = open("deobf.txt","r").readlines()
result = str(open("env.txt","r").read())
for line in file:
    if line.startswith("Set"):
        name = line.split(" ")[1].strip().split("=")[0]
        rep = line.split(" ")[1].strip().split("=")[1]
        if rep == "<":
            rep = " "
        result = result.replace("%"+name+"%", rep)

print(result)
