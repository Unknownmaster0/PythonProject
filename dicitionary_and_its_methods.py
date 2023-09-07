# representation of set and dictionary is same. {}
# But difference in empty set and empty dictionary

# initialising empty dictionary
a = {}
print(a,type(a))
b = set()
print(b,type(b))

# dictionary is something kind of mapping in C++
marks = {"sagar": 99, "satyam": 87, "shalu": 100, "Aashu": 65, "Bhaiya": 54}
print(marks)

print("printing only values of marks->",marks.values())
print("printing only keys of marks->",marks.keys())
print("printing the items of marks->",marks.items())
print("pop one element from marks->",marks.pop("Bhaiya"))
print("size of marks->",marks.__sizeof__())

