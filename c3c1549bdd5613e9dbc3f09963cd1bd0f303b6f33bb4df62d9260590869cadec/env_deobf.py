import sys

def parse_line(line):
    variable_list = []
    percent = False
    temp = ""
    for char in line:
        if char != "%" and percent == True:
            temp += char
        if char == "%" and percent == False:
            percent = True
            continue
        if char == "%" and percent == True:
            percent = False
            variable_list.append(temp)
            temp = ""
    return variable_list

variables = dict()
file = open("Regge.dif","r").readlines()

for line in file:
    line = line.strip()
    if "%" not in line and "Set" not in line:
        continue

    if "Set" in line:
        name = line.split(" ")[1].split("=")[-2]
        value = line.split(" ")[1].split("=")[-1]
        variables[name] = value
        continue
    if "%" in line:
        for variable in parse_line(line):
            if variable in variables:
                line = line.replace("%"+variable+"%", variables[variable])
    
        
        if "Set" in line:
            name = line.split(" ")[1].split("=")[0]
            value = line.split(" ")[1].split("=")[1]
            variables[name] = value
            
    print(line)

    
        
