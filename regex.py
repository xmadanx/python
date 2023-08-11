import re
s = input()
d = re.findall(r'[\d]{4}', s)
md = [eval(i) for i in d]
l = min(md)
h = max(md)
if (l == h):
	print(1)
else:
	print(h-l)

