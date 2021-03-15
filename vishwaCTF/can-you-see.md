# Can U See?

```python
a = """1 0 1 0 1 0 1 0 1 1 0 1 1 1 1 1 0 0 1 1 0 1 0 1 1 1 1 1 0 1 1 1 0 1 0 1 1 1 1 0 0 1 1 0 0 0 1 0 1 0
1 0 1 0 1 1 0 1 0 1 0 1 0 0 0 0 0 1 0 1 1 0 0 1 0 0 0 1 0 1 0 0 1 0 0 1 1 1 0 1 0 1 0 1 0 1 0 1 0 1
1 1 1 1 0 0 1 0 1 0 1 1 0 0 0 0 0 1 0 0 1 0 1 1 0 0 1 1 1 1 0 0 1 0 1 1 0 0 1 0 1 1 0 0 0 1 0 0 0 0"""
t= []
for i in a.split("\n"):
	t.append(i.split(" "))
res = []
for i in range(len(t[0])):
	for j in range(len(t)):
		res.append(t[j][i])

c  = ''.join(res)

res = [c[i:i+6] for i in range(0, len(c), 6)]
print(' '.join(res))

# 111001 111001 110010 101010  101110 001111 100100 100100 000011 100110 011100  001111 100100 101111 001111 100100 011100  001111 110110 101010  001111 100010 000011 100010 100010
```
Manually match to bits to dots for the flag on https://www.dcode.fr/braille-alphabet
