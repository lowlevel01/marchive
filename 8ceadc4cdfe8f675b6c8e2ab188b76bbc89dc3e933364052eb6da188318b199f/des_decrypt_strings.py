from Crypto.Cipher import DES
from Crypto.Hash import MD5
import base64

def dec(string_61, string_62):
    try:
        md5_hash = MD5.new(string_62.encode('ascii')).digest()  # Compute MD5 hash
        des_key = md5_hash[:8]  
        cipher = DES.new(des_key, DES.MODE_ECB)

        encrypted_data = base64.b64decode(string_61)

        decrypted_data = cipher.decrypt(encrypted_data)


        padding_length = decrypted_data[-1]
        decrypted_data = decrypted_data[:-padding_length] 
        result = decrypted_data.decode('ascii') 

    except Exception as ex:
        result = None

    return result

