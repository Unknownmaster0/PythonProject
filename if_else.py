# else if -> elif in python

age = int(input("enter your age: "))

if(age >= 18):
    print("Yes, you can vote.")
elif(age < 10):
    print("you are baby booner.")
elif(age >= 10 and age < 18):
    print("You are teen now.")