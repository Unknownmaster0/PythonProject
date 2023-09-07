# tuple are same as list but they are immutable as string.
# means they can't be changed.
# tuple are assigned in parenthesis ()

t = (2,3,4,7,1,2)
# we can't change this made tuple.
print(t)
print("try to make some changes in tuple.")
print("index of 2 ->",t.index(2))
print("occurrence of 2 ->",t.count(2))
# print("index of 100 ->",t.index(100))  #  this will give error as 100 is not in tuple.

t2 = (3,4,5,'sagar')
print(t2)

