# list in python
"""
there is difference between list and string.
string -> they are immutable. Every time the python need to create the new string for the changes you make.
list -> they are mutable. They don't need to create every time after every changes.
"""
print("learning list in python.")
l1 = [2, 3, 5, "sagar"]
print(l1)

print("list can be modified using the methods they provide to us.")
print("count of 3 ->", l1.count(3))  # count method
l1.append(689)  # append method
print("after appending 689 in list -> ")
print(l1)

print("the index of 2 ->",l1.index(2))
print("the index of 3 ->",l1.index(3))
print("the index of 5 ->",l1.index(5))

l2 = [87,54,12,9,43,189]
print("list l2 ->",l2)
print("sorting the l2 list.")
l2.sort()

print("after sort the list becomes->",l2)

print("pop method in list -> remove the last element of list.")
l2.pop()
print(l2)

print('element at 0th index of l1->',l1[0])
# we can change the list element as they are mutable.
l1[2] = 'website'
print("after changing the element of list1.")
print(l1)

