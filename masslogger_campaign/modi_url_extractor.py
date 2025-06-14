import re

def extract_big_hex(text, min_length=600):
    pattern = rf'\b[0-9a-fA-F]{{{min_length},}}\b'
    return re.findall(pattern, text)


file = open("output.vbs","r").read()

big_hexes = extract_big_hex(file)


interesting = []

for hex in big_hexes:
    if hex.startswith("0000"):
        interesting.append(hex[::-1])

file = open("modi_loader", "wb")
file.write(bytes.fromhex(interesting[2]))


with open("modi_loader", "rb") as f:
    data = f.read().decode("utf-16-le", errors="ignore")
    ascii_bytes = data.encode('ascii', 'ignore')
    ascii_text = ascii_bytes.decode('ascii')


pattern = re.compile(r'https?://\S+')
matches = pattern.findall(ascii_text)

print(matches)
