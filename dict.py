#Ordered
#Changeable
#Duplicates not allowed

a = {
	"phone" : "Iphone 13 pro max",
	"laptop" : "Macbook pro",
	"headphone" : "Airpods pro"
}

print(a)
"""
{'phone': 'Iphone 13 pro max', 'laptop': 'Macbook pro', 'headphone': 'Airpods pro'}
"""
a["tablet"] = "Ipad pro"

print(a)
"""
{'phone': 'Iphone 13 pro max', 'laptop': 'Macbook pro', 'headphone': 'Airpods pro', 'tablet': 'Ipad pro'}
"""
a["laptop"] = "Macbook pro 14"

print(a)
"""
{'phone': 'Iphone 13 pro max', 'laptop': 'Macbook pro 14', 'headphone': 'Airpods pro', 'tablet': 'Ipad pro'}
"""
for i in a:
	print(i)
"""
phone
laptop
headphone
tablet
"""
for i in a:
	print(a[i])
"""
Iphone 13 pro max
Macbook pro 14
Airpods pro
Ipad pro
"""
for i,j in a.items():
	print(i,j)
"""
phone Iphone 13 pro max
laptop Macbook pro 14
headphone Airpods pro
tablet Ipad pro
"""




