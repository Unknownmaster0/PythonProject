# printing the numbers in range.
# keywords -> break , continue
# it will run till n-1
for i in range(2,5):
    if(i == 3):
        continue
    print(i)

print("printing number from 1 to 5.")
for i in range(5):
    if(i == 4):
        break
    print(i+1)

# loops can be used to print the data sets,dictionary,tuple,list and many thing.
marks = {"sagar": 99, "satyam": 87, "shalu": 100, "Aashu": 65, "Bhaiya": 54}
print("printing the key of dictionary.")
for item in marks:
    print(item)

print("printing the values of dictionary.")
for item in marks.values():
    print(item)