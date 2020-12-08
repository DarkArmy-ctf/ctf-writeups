from pwn import *
import binascii
from Crypto.Util.Padding import pad,unpad

# nc 157.230.237.229 2200
r = remote("157.230.237.229", 2200)
print(r.recv().decode())

"""
1. Enter key and get flag
2. Encrypt plaintext
3. Decrypt ciphertext
"""
option = '3'
print(option)
r.sendline(option)
print(r.recv().decode())

"""
THE ATTACK
==========
Ref: https://blog.h25.io/SwampCTF-AES/

XORing with zeros does nothing (0 is the identity element of XOR), so we have

Output1 xor Output2 = (decryptAES(0000000000000000, key) xor IV) xor decryptAES(0000000000000000, key)
Output1 xor Output2 = IV xor decryptAES(0000000000000000, key) xor decryptAES(0000000000000000, key)
Output1 xor Output2 = IV xor (decryptAES(0000000000000000, key) xor decryptAES(0000000000000000, key))
Output1 xor Output2 = IV xor 0000000000000000
Output1 xor Output2 = IV
"""
# STEP 1: Send known ciphertext to decrypt
ciphertext = '0'*96
print(ciphertext)
r.sendline(ciphertext)

# STEP 2: Receive plaintext
recv_pl = r.recv().decode().strip()
print(recv_pl)
plaintext = recv_pl.split(':  ')[1]
# print(plaintext)

# STEP 3: Take adjacent 32 bytes of decrypted plaintext in chunks of BLOCK_SIZE = 16 (32 without hex decode)
pblock1 = plaintext[:32]
pblock2 = plaintext[32:64]

# STEP 4: Recover the IV by XORing the chunks
iv = hex( int(pblock1, 16) ^ int(pblock2, 16) )[2:]
print(iv)

assert len(iv) == 32


print(r.recv().decode())
option = '1'
print(option)
r.sendline(option)
print(r.recv().decode())
print(iv)
r.sendline(iv)
r.interactive()