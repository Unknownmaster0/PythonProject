# making the class is important to use for the template

class student:
    # constructor call in classes.
    def __init__(self,name,stream):
        self.name = name
        self.stream = stream

    # get function in classes
    def getStream(self):
        return self.stream

s1 = student("sagar","science")
print("name of s1 ->", s1.name)
print("stream of s1 ->", s1.stream)