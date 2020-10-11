from Crypto.Cipher import AES
from base64 import b64decode, b64encode
import json

def encrypt_file(key, filepath):
    cipher = AES.new(key, AES.MODE_OCB)

    file_text = b''
    with open(filepath, 'rb') as fin:
        file_text = fin.read()
    chipher_text, tag = cipher.encrypt_and_digest(file_text)
    json_k = [ 'nonce', 'cipher_text', 'tag' ]
    json_v = [ b64encode(item).decode('utf-8') for item in [cipher.nonce, chipher_text, tag] ]
    return json.dumps(dict(zip(json_k, json_v)))

def decrypt_file(key, nonce, cipher_text, tag):
    cipher = AES.new(key, AES.MODE_OCB, nonce = nonce)
    return cipher.decrypt_and_verify(cipher_text, tag)