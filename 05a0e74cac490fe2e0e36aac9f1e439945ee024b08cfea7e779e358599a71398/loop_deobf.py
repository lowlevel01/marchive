import re

def deobfuscate_all_loops(content):

    while_pattern = re.compile(
        r'While\s+(\d+)\s*\n(.*?)WEnd',
        re.DOTALL | re.IGNORECASE
    )

    def process_while_loop(match):
        loop_body = match.group(2)

        switch_pattern = re.compile(
            r'Switch\s*(\$\w+)\s*(.*?)EndSwitch',
            re.DOTALL | re.IGNORECASE
        )
        switch_match = switch_pattern.search(loop_body)

        if not switch_match:
            return match.group(0) 

        switch_var = switch_match.group(1)
        cases = re.findall(
            r'Case\s+(\d+)\s*\n(.*?)(?=\n\s*Case|\n\s*EndSwitch)',
            switch_match.group(2),
            re.DOTALL
        )

        real_case = None
        for case_num, case_code in cases:
            if 'ExitLoop' in case_code:
                real_case = case_code
                break

        if not real_case:
            return match.group(0)  

        clean_code = re.sub(
            r'\$[\w]+\s*=\s*\$\w+\s*\+\s*\d+\s*/\s*\d+',
            '',
            real_case
        )

        clean_code = clean_code.replace('ExitLoop', '')

        clean_code = '\n'.join(line.strip() for line in clean_code.splitlines() if line.strip())

        return clean_code.strip()

    return while_pattern.sub(process_while_loop, content)


def main():
    with open('second.au3', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    deobfuscated_content = deobfuscate_all_loops(content)

    with open('cleaned.au3', 'w', encoding='utf-8') as f:
        f.write(deobfuscated_content)



if __name__ == '__main__':
    main()