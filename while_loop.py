i = 0
while(i < 10):
    print(i)
    i += 1


# infinite loop
while(True):
    num = int(input("0 to exit and any number to continue: "))
    if(num == 0):
        break
    print(num)