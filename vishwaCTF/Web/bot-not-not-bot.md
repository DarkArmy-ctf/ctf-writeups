```python
import request
for i in range(1,501):
	x = requests.get("https://bot-not-not-bot.vishwactf.com/page"+str(i)+".html",verify=False)
	if "Useless" not in x.text:
		print(x.text)


```
Manually arrange the flag char with its index
