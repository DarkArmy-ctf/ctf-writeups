# Musical Mix-up
## Forensics Challenge

### Description:
>One of our guys found a strange midi file lying around on our servers. We think there might be some hidden data in it. See if you can help us out!

[chalenge.mid]

### Overview:
Initially it looks like theres some kind of instrument recording in challenge.mid.
MIDI files can be converted to csv files with information on tone velocity and so on.
This can be done using a python script with python module py_midicsv
To install the python module:
```
pip3 install py_midicsv
```
`midi_to_csv('file.mid')` is the function we need to convert MIDI file to csv.

##### Sample Script:
```
import py_midicsv as pm

csv_string = pm.midi_to_csv("challenge.mid")
print(csv_string)

f = open('challenge.csv', 'a')

for i in csv_string:
	print(i,end='')
	f.write(i)
f.close()
```

Opening the csv file we see that the 5th and the 6th field have only numbers. and the initial numbers are within ascii range.
The can be extracted and converted with a script
The 5th field does not give us anything useful.
But the 6th field converts to the flag:
To extract and convert to ascii:
##### Sample Script:
```
with open('challenge.csv','r') as f:
	data = f.read().split('\n')

ascii = ''

for i in data:
	try:
		i = int(i.split(', ')[-1])
		ascii += chr(i)
	except:
		continue
	
print(ascii)
```

### Flag:
ractf{f50c13ty_l3vel_5t3g!}
