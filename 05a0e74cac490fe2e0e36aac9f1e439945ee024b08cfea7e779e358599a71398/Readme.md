
# Family : probably Lumma Stealer

- INS installer which is an SFX Archive with installation script and some Aretfecats disguised as PDF Files
- Installer script runs a batch script disguised as a pdf file which is obfuscated by means of environment variables (each command can be deobfuscated with enc_deobf.py)
- The batch script checks for presence of AV software, introduces some delays and extracts a Cabinet file
- The rest of the PDF Files are combined to form an AutoIt runner and the files the cabinet files are combined to form an AutoIt file
- The AutoIt script in the AutoIt file was obfuscated in two ways: <br>
    1- Strings are obfuscated with a certain function (string_deobf.py can deobfuscate them)
    2- While loops that intitiate a variable in a certain way and use the switch statemet to hit only a single case and leave afterwards rendering the rest of the cases useless (loop_deobf.py can deobfuscate them)
