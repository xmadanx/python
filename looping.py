#Not the easy Way

"""
d = [1]
j=0
for i in d:
    d.append(1)
    j+=1
    if j<5+1:
        print("Love you")
    else:
        break
"""

#Best Way

i=0
for _ in iter(int,1):
    if i<5:
        print("Love you")
        i+=1
    else:
        break

#Run for loop infinitely

"""
for _ in iter(int,1):
    print("Hello")
"""

