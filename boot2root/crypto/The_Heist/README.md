# The Heist (496)
> A heist was carried out in the Royal Bank of Spain recently, Benjamin (one of the hostages) was able to transmit a message through a buggy AES server. <br>
> The police has to find this message to plan their next move. Find this message and help the police save those hostages. <br>
> `nc 157.230.237.229 2200` <br>
> [:arrow_down: chall.py](chall.py)

## Solution
Weak AES Encryption with **Key = IV** something like this -> [https://cryptopals.com/sets/4/challenges/27](https://cryptopals.com/sets/4/challenges/27)

A moment after connectintion,
```console
root@kali:~/Downloads/b00t2r00t/crypto# nc 157.230.237.229 2200

1. Enter key and get flag
2. Encrypt plaintext
3. Decrypt ciphertext

Enter option: 
```
### Solve Script: [apex.py](apex.py)
```py
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
```
### Output:
```console
root@kali:~/Downloads/b00t2r00t/crypto/heist# python3 apex.py 
[+] Opening connection to 157.230.237.229 on port 2200: Done

1. Enter key and get flag
2. Encrypt plaintext
3. Decrypt ciphertext

Enter option: 
3
Enter hex ciphertext: 
000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
Plaintext:  1d8dec46a622bc7f2dd8d3236262a4866de29c23df47c81748abb24a0e0dd6f46de29c23df47c81748abb24a0e0dd6f4
706f706579657468657361696c6f7272

1. Enter key and get flag
2. Encrypt plaintext
3. Decrypt ciphertext

Enter option: 
1
Enter hex key: 
706f706579657468657361696c6f7272
[*] Switching to interactive mode
b00t2root{th3y_4r3_g0ing_t0_k1ll_u5}
[*] Got EOF while reading in interactive
$ 
[*] Interrupted
root@kali:~/Downloads/b00t2r00t/crypto/heist# 
```
## Flag
> **b00t2root{th3y_4r3_g0ing_t0_k1ll_u5}**

<details><summary>SEO</summary>
    AES, AES-CBC, AES Cryptography, Key=IV in AES, Weak AES, Recover the key from CBC with IV=Key
</details>
