"""
You can open a file in three modes in the most of programming languages including Python.
1. read -> r
2. write -> w
3. append -> a
"""

# Reading to the file.
with open("sagar.txt","r") as f:
    s = f.read()
    print(s)

# the above whole thing can also be written in another way as :
"""
f = open("sagar.txt", "r")
s = f.read()
print(s)
f.close()
"""

# appending to the file.
with open("sagar.txt", "a") as f:
    f.write("He is also the nice guy.")

# the above whole thing can also be written in another way as :
"""
f = open("sagar.txt","a")
f.write("He is also the nice guy.")
f.close()
"""

# writing to the file. -> this will lost the content of the file which left earlier.
with open("sagar.txt", "w") as f:
    f.write("My all content has gone.")
