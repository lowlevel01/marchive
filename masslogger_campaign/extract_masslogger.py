# Extracts masslogger executable from the VBS file

import re

def extract_big_hex(text, min_length=600):
    pattern = rf'\b[0-9a-fA-F]{{{min_length},}}\b'
    return re.findall(pattern, text)



file = open("output.vbs","r").read()

big_hexes = extract_big_hex(file)

dll = bytes.fromhex(big_hexes[3][::-1])


mass = open("mass","wb")
mass.write(dll)
