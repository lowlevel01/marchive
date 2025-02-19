import re
import base64

def obf_replace(line):
    line = line.strip().replace(" ","").replace("\n","").replace("\t","")
    obfuscated = re.findall(r'\{([^}]+)\}', line)[0]
    obfuscated = obfuscated.replace("'","").replace(",","")
    other_part = re.findall(r'\(([^}]+)\)', line)[0].split(",")
    to_be_replaced = other_part[0][1:-1]

    replacement = other_part[1]
    while(replacement[-1] == ")"):
        replacement = replacement[:-1]

    if(replacement == "string.Empty"):
        obfuscated = obfuscated.replace(to_be_replaced, "")
    else:
        obfuscated = obfuscated.replace(to_be_replaced, replacement[1:-1])

    return obfuscated

def b64_replace(line):
    return base64.b64decode(obf_replace(line))

print(obf_replace("""new string(new char[]
					{
						'%', 'U', 'S', 'E', 'R', 'P', 'H', 'e', 'a', 'l',
						't', 'h', 'R', 'O', 'F', 'I', 'L', 'E', '%', '\\',
						'A', 'p', 'p', 'H', 'e', 'a', 'l', 't', 'h', 'D',
						'a', 't', 'a', '\\', 'R', 'o', 'a', 'm', 'H', 'e',
						'a', 'l', 't', 'h', 'i', 'n', 'g'
					}).Replace("Health", string.Empty))"""))
print(b64_replace("""
Encoding.UTF8.GetString(Convert.FromBase64String(new string(new char[]
					{
						'Y', '2', '9', 'v', 'a', '2', 'l', 'l', 'c', 'y',
						'5', 'L', 'a', 'n', 'g', 'u', 'a', 'g', 'e', 'z',
						'c', 'W', 'x', 'p', 'd', 'G', 'U', '='
					}).Replace("Language", string.Empty)))"""))
