a = ["the","quick","brown","fox","jumps","over","the","lazy","dog"]
b = [1,7,4,2]
a.sort()
print(a)
"""
['brown', 'dog', 'fox', 'jumps', 'lazy', 'over', 'quick', 'the', 'the']
"""
a.sort(reverse = True)
print(a)
"""
['the', 'the', 'quick', 'over', 'lazy', 'jumps', 'fox', 'dog', 'brown']
"""
b.sort()
print(b)
"""
[1, 2, 4, 7]
"""
b.sort(reverse = True)
print(b)
"""
[7, 4, 2, 1]
"""
for i in a:
  print(i)
"""
the
the
quick
over
lazy
jumps
fox
dog
brown
"""
for i in b:
  print(i)
"""
7
4
2
1
"""
