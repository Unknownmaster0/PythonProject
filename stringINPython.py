# string in python
name = 'sagar'

print(name)

# printing the half or some portion of the name.
print(name[0:3])  # this will print the 0 to (3-1) characters of the name
print(name[4:7])  # this will print the all the characters that in its range. And doesn't give any error.
print(name[5:7])  # this will give no error and simply doesn't print anything, when we write outside the boundry of string.

# kitne tareke se string ko likh sakte hai python me.
print("different ways to initialise the string in python.")
name1 = 'sagar'
name2 = "sagar"
name3 = '''sagar'''

print(name1, name2, name3)


# methods in strings in python
print(name.count("a"))  # count the occurrence of given character in string.
print(name.capitalize())  # capitalise the first character of the string.
print(name.isalnum())  # check if the string is alphanumeric or not.
