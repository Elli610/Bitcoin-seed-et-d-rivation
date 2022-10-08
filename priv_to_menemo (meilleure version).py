import secrets
import hashlib
import hmac
import ecdsa
import codecs
import data as d

def get_random_bytes(num_bytes):
    return secrets.token_bytes(num_bytes)

#print(get_random_bytes(16))

def priv_to_mnemo(priv):
    """
    input : private key (bytes)
    output : mnemonic (str)
    """
    checksum = bytes_to_bin(hashlib.sha256(priv).digest())[:4]
    
    print("checksum : ", checksum)
    print("priv : ", bytes_to_bin(priv))
    key = bytes_to_bin(priv) + checksum
    key2 = ""
    for i in range(0, len(key), 11):
        if (key[i] == "1" or key[i] == "0"):
            key2 = key2 + key[i]
    return ' '.join(d.wordlist[int(key[11*i:(i+1)*11], 2)] for i in range(0, 12))

def bytes_to_bin(b):
    """
    input : bytes
    output : binary string
    """
    return ''.join(format(x, '08b') for x in b)


a = get_random_bytes(16)
print (a)
print(priv_to_mnemo(a))




