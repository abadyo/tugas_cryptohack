#!/usr/bin/env python3

from Crypto.Cipher import AES

import requests
import hashlib
import sys
import binascii

# 1
# result1 = requests.get('https://aes.cryptohack.org/block_cipher_starter/encrypt_flag/')
# ciphertext_hex = result1.json()["ciphertext"]
# print(ciphertext_hex)

# result2 = requests.get(f"https://aes.cryptohack.org/block_cipher_starter/decrypt/{ciphertext_hex}")
# plaintext = result2.json()["plaintext"]
# print(binascii.unhexlify(plaintext).decode())



# 2
# result = requests.get('https://aes.cryptohack.org/passwords_as_keys/encrypt_flag')
# ciphertext_hex = result.json()["ciphertext"]

# with open('words', 'r') as f:
#     for word in f:
#         word = word.strip()
#         attempted_key = hashlib.md5(word.encode()).hexdigest()

#         ciphertext = bytes.fromhex(ciphertext_hex)
#         key = bytes.fromhex(attempted_key)
#         cipher = AES.new(key, AES.MODE_ECB)
#         try:
#             decrypted = cipher.decrypt(ciphertext)
#             result = binascii.unhexlify(decrypted.hex())
#             if result.startswith('crypto{'.encode()):
#                 print("key is %s" % word)
#                 print(result.decode('utf-8'))
#                 sys.exit(0)
#         except ValueError as e:
#             continue

# 3
# tes = 'abad'.encode()
# print(binascii.hexlify(tes))

# def ascii_to_hex(string: str) -> str:
#     return ''.join([hex(ord(c))[2:] for c in string])

# def get_letter(block, depth=1):
#     block = block[-31:]
#     trail = block[:32 - depth]

#     for letter in 'abcdefghijklmnopqrstuvwxyz1234567890_{}':
#         plaintext = ascii_to_hex(block + letter + trail)

#         response = requests.get('http://aes.cryptohack.org/ecb_oracle/encrypt/' + plaintext)
#         ciphertext = response.json()['ciphertext']

#         if ciphertext[32:64] == ciphertext[96:128]:
#             current_flag = block + letter
#             print(current_flag)
#             if letter != '}':
#                 return get_letter(current_flag, depth + 1)
#             else:
#                 return current_flag.lstrip('-')

#     return block.lstrip('-')

# flag = get_letter('-' * 32)
# print("The flag is: " + flag)
#crypto{p3n6u1n5_h473_3cb}

# 4 
# crypto{3cb_5uck5_4v01d_17_!!!!!}
# def xor(a,b):
#     a = bytes.fromhex(a)
#     b = bytes.fromhex(b)
#     return bytes(i ^ j for i,j in zip(a,b))


# cipher = requests.get('http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/')
# cipher = cipher.json()['ciphertext']

# iv = cipher[:32]
# cipher1 = cipher[32:64]
# cipher2 = cipher[64:96]

# decrypt2 = requests.get('http://aes.cryptohack.org/ecbcbcwtf/decrypt/' + cipher2 + '/')
# decrypt2 = decrypt2.json()['plaintext']
# decrypt2 = xor(decrypt2,cipher1)

# decrypt1 = requests.get('http://aes.cryptohack.org/ecbcbcwtf/decrypt/' + cipher1 + '/')
# decrypt1 = decrypt1.json()['plaintext']
# decrypt1 = xor(decrypt1,iv)

# print(decrypt1+decrypt2)