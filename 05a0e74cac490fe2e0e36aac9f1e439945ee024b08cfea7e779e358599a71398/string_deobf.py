import re

def evaluate_autoit_expression(expr):

    try:
        result = eval(expr)
    except:
        return 0  
        
    result = result % (1 << 32)
    if result >= (1 << 31):
        result -= (1 << 32)
    return result

def decode_born_string(encoded_str, sub_value):
    parts = encoded_str.split('J')
    decoded = []
    for part in parts:
        try:
            char_code = int(part) - sub_value
            decoded.append(chr(char_code))
        except:
            decoded.append('�')
    return ''.join(decoded)

def deobfuscate_script(input_path, output_path):
    """
    Process the AutoIt script to decode BORN obfuscation
    """
    with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    pattern = re.compile(r'(?i)BORN\s*\(\s*"([^"]+)"\s*,\s*([^)]+)\s*\)', re.IGNORECASE)
    
    def replace_match(match):
        encoded_str = match.group(1)
        expr = match.group(2).strip()
        sub_value = evaluate_autoit_expression(expr)
        decoded = decode_born_string(encoded_str, sub_value)
        return f'"{decoded}"'  # Replace with decoded string

    deobfuscated = pattern.sub(replace_match, content)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(deobfuscated)

input_file = "cleaned.au3"
output_file = "deobfuscated.au3"

deobfuscate_script(input_file, output_file)
print(f"Deobfuscation complete. Saved to {output_file}")
