# 007 (484)
> Who is this 007? <br>
> [:arrow_down: 007.py](007.py)

# Solution
### Solve Script: [apex.py](apex.py)
```py
import base64

# ROT Cipher Implementation (shamelessly copied from the encryption script)
def rot(s, num):
	l=""
	for i in s:
		if(ord(i) in range(97,97+26)):
			l+=chr((ord(i)-97+num)%26+97)
		else:
			l+=i
	return l


cipher = base64.b64decode("MRU2FDcePBQlPwAdVXo5ElN3MDwMNURVDCc9PgwPORJTdzATN2wAN28=")

val = []
for i in cipher:
	val.append(i)
print(val)

"""
Recover 1st char of the base64 encoded string

recovered_string = X X A w X X X X X ... [flag format "b00t2root"]
"""
c1 = val[1] ^ ord('A')
c0 = val[0] ^ c1
# print(chr(c0), chr(c1))

kp = c0
r = chr(c0)
for i in val:
	r += chr(i ^ kp)
	kp = i ^ kp

# Check recovered string
print(r.encode())
r = base64.b64decode(r).decode()
print(r)

# Brute-force ROT cipher
for i in range(1,26):
	flag = rot(r, i)
	if 'b00t' in flag:
		print(f"\nFlag:\n{flag}")
```
## Flag
> b00t2root{Bond. James Bond.}
