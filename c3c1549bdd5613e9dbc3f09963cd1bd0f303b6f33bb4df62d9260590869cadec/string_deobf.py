import re


def decode(array, shift):
    array = array.split("]")
    result = ""

    for element in array:
        result += chr(int(element) - shift)
    return result

obf_func = "xrgZuSp"

regex = r'xrgZuSp\("([\d\]]+)"\s*,\s*(\d+)\)'


file = open("Tuo.dif","r").read()

matches = re.findall(regex, file)

for match in matches:
    array = match[0]
    shift = int(match[1])
    decoded_string = "\""+decode(array, shift)+"\""
    to_be_replaced = obf_func+"(\""+match[0]+"\","+match[1]+")"
    file = file.replace(to_be_replaced, decoded_string)


output = open("deobfuscated_strings.dif","w")
output.write(file)
