from autoit_ripper import extract, AutoItVersion

with open("sample.exe", "rb") as f:
    file_content = f.read()


def extract_repeating_pattern(s):
    n = len(s)
    z = [0]*n
    for i in range(1, n):
        while i + z[i] < n and s[z[i]] == s[i+z[i]]:
              z[i] += 1

    last_index = z.index(max(z))
    return s[:last_index]

content_list = extract(data=file_content, version=AutoItVersion.EA06)

enc_exe = content_list[2][1]

    
dos_header = b"\x4D\x5A\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00\xFF\xFF\x00\x00\xB8\x00\x00\x00\x00\x00\x00\x00\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x01\x00\x00"


includes_key = ""
for (dos, enc) in zip(dos_header, enc_exe):
    includes_key += chr(dos ^ enc)

key = extract_repeating_pattern(includes_key)

enc_exe = bytearray(enc_exe)
for i in range(len(enc_exe)):
    enc_exe[i] = enc_exe[i] ^ ord(key[i % len(key)])
with open("stage2.exe", "wb") as stage2:
    stage2.write(enc_exe)
        
