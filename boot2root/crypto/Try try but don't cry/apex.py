import base64, string

def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)).decode() == s
    except Exception:
        return False

def isHex(s):
	return all(c in string.hexdigits for c in s)

def xor(a,b):
	l=""
	for i in range(min(len(a), len(b))):
		l+=chr(ord(a[i]) ^ ord(b[i]))
	return l

data = open('chall.txt').read().strip()
c=0
while 1:
	if isHex(data):
		print(f"[{c}] \t Found : Hex")
		data = bytes.fromhex(data).decode().replace('\n','')
		c+=1
	elif isBase64(data):
		print(f"[{c}] \t Found : Base64")
		data = base64.b64decode(data).decode().replace('\n','')
		c+=1
	
	# print(data)
	if len(data) == 22:
		print(f"\n[+] Got it : {data}")
		break

last = xor(chr(int(data[-2:], 16)), '}')
# print(last)
known = "b00t2root{" + last
data = bytes.fromhex(data).decode()
last11 = xor(data, known)
# print(last11)

flag = known + last11

print(f"\n[+] Flag:\n{flag}")