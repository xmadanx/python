#Unordered
#Unchangeable
#Duplicates not allowed

a = {1,7,4,2}
print(a)                                         # {1, 2, 4, 7}

a.add(0)
print(a)                                         # {0, 1, 2, 4, 7}

a.remove(1)
#if the element is not in the set it gives error
a.discard(5)
# Use discard it does'nt shows error
print(a)                                         # {0, 2, 4, 7}



