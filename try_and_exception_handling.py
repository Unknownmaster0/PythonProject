"""
sometimes we get error, and we don't want to stop our program due to this error.
Thus, we use try and exception handling method in python.


here we use as integer veriable, but what happen if we give input as string.
Then, it will throw error,make stop to our program at that instant.
To avoid this, we do, use 'try and exception' method.
"""

try:
    a = int(input("enter the number: "))
    print(a + 5)
except Exception as e:
    print("Error! occurred due to -> ", e)


# don't use try and except and then try to run this program and give user input as string. The program will stop with some errors.