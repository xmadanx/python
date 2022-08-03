#Changeable
#Allow duplicates
#Different data types

a = ["i", "love", "you","python"]
print(a)                           # ['i', 'love', 'you', 'python']

print(a[0])                        # i
print(a[1])                        # love
print(a[-1])                       # python

#indexing
print(a[1:-1])                     

#replace elements
a[0] = "we"

#insert elements
a.insert(1,"all")

#append elements
a.append("c")

for i in a:
    print(i)

if "python" in a:
    print("We love python")
else:
    print("Its not python")

