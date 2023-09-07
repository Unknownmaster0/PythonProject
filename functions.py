# we can use the defined word 'def' to initialise function

# This function is not execute first, until and unless no-one call it.
def average(a,b):
    return (a+b)/2

print("average of 3 and 4 is ->",average(4,5))


# function which will not return anything.
def greeting(name,greet):
    print("Hii "+name+" good morning.")
    print(greet+" for calling me.")

greeting("sagar","thanks")


# letter generator function
def letter(name,date):
    s = f"Hello sir,\nThis is {name}.I am regret to say that I will not able to attend your lecture on {date} ,due to health issue. I will continue the class from Monday onwards."
    print(s)


print("generating the letter for myself.")
s = input("enter name: ")
d = input("enter date: ")
letter(s,d)