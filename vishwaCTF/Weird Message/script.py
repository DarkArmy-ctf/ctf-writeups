from PIL import Image
f = open("weird.txt")
data = f.read().decode()

img = Image.new( 'RGB', (1226,42), "black")
pixels = img.load()

c = 0

for i in range(41):
	for j in range(1226):
		if(int(str(data[c])) == 0):
			pixels[j,i] = (0,0,0)
		else:
			pixels[j,i] = (255,255,255)
		c += 1
img.show()
