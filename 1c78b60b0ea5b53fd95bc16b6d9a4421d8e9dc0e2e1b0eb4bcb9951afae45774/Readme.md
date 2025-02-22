
### stage2.py extracts the stage 2 sample.

### Details for curious people:
  - I extracted the AutoIt artefacts using the autoit_ripper module
  - There were the AutoIt script and two other files
  - One of the file was an executable encrypted in Xor which is loaded by the AutoIt script after decryption
  - I didn't want my code to be dependent on the key.
  - I recalled the DOS Stub is the same in all PE files
  - I xored with the DOS Stub to get the key. The repeating pattern is the key
  - I didn't want my code to be dependent on the length of the key
  - So, I used Z-transform algorithm (string algorithm I learned while doing some competitive programming) to extract the pattern
  - I Xored with the key and got stage 2
