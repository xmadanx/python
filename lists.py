#Changeable
#Allow duplicates
#Different data types

a = ["i", "love", "you","python"]
print(a)                           # ['i', 'love', 'you', 'python']

print(a[0])                        # i
print(a[1])                        # love
print(a[-1])                       # python

#indexing                       
print(a[1:-1])                     # ['love', 'you']

#replace elements
a[0] = "we"                        

#insert elements
a.insert(1,"all")

#append elements
a.append("c")

for i in a:
    print(i)
"""
we
all
love
you
python
c
"""

if "python" in a:                  # We love python
    print("We love python")
else:
    print("Its not python")

