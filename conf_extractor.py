import os
import sys
import re
import base64


#if len(sys.argv) < 2:
#    print("Usage : conf_extractor.py [PATH]")

#path = sys.argv[1]
path = "sample.exe"
os.system("ilspycmd -p "+path+" -o .\decompiled")

def xor_decrypt(data, key):
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])
def StringDecrypt(encoded_str, key):
    decoded_data = base64.b64decode(encoded_str)
    decrypted_data = xor_decrypt(decoded_data, key)
    final_result = base64.b64decode(decrypted_data)
    return final_result


with open(".\decompiled\Arguments.cs","r") as args:
    elements = re.findall("\"([^;]*)\"", args.read())
    ip = elements[0]
    if ":" in ip:
        print("The config is not encrypted\n C2: "+ip)
    else:
        key = elements[3]
        print("Decrypted C2 : "+StringDecrypt(ip, key))
