# what is set? -> initialized with { } and never return the duplicate element.
# it may have duplicate element but can't ever print or return the duplicate element.

# initialising the empty set
a = set()
print(a,type(a))
print(a.__sizeof__())

# initialising set.
s1 = {1,2,3,1,1,2,3,89,6}
s2 = {"sagar",4,65,-89,"singh"}
print("set1 is ->",s1)
print("size of set1 ->",s1.__sizeof__())
s1.add(-1)
print("set1 becomes ->",s1)
print("popping element from set1->",s1.pop())
# s1[2] = 5  # they are also immutable.'set' object does not support item assignment
# print(s)

print("set2 ->",s2)

print("printing the union of set1 and set2")
print(s1.union(s2))
print(s1.intersection(s2))  #  it return the intersection of two sets -> if no elements is common it will return this-> set()