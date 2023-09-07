# variable in python
a = 3
print(a)

# printing the variables in python
a = 6.2
print(a)

# Note that the same variable name can store different type of data types.
a = "sagar"
print(a)

a = None  # a new data type in python
print(a)

# Type-Casting in python
s = "5"
print(s)
# here s and t are holding the same value but there data type is different. Here, s is string and t is integer.
t = 5
print(t)

# difference come in both when we add any number in both
# print(s+1)  # this line will throw error, so we use typecasting technique.
print( int(s) + 1)  # here we type-casted the string to integer
print(t+1)

# You can know the type of data type of the variable -> simply by writing = type(name of variable)
print("Knowing the type of variable.")
a = 'sagar'
print("type of a->",type(a))
a = 6
print("type of a->",type(a))
a = True
print("type of a->",type(a))

