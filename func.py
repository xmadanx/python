def name():
	print("Madan")                      

def age():
	return(21)

name()                                    # Madan
print(age())                              # 21

#Arguments

def add(x):
	print(x + 5)
add(2)                                    # 7

#x=5 is a default value

def add(x=5):           
	print(x + 5)
add()                                     # 10
add(3)                                    # 8

# * is used for multiple arguments

def add(*x):
	print(x[0] + x[1])

add(5,6)                                  # 11

# ** is used for multiple keyword arguments

def add(**x):
	print(x["first"] + x["second"])

add(first=10,second=15)                   # 25




