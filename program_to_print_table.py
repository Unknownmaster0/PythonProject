# This program is for printing the table from 1 to 10 using match cases

a = int(input("enter number b/w 1 to 10: "))

match a:
    case 1:
        print(1*1,1*2,1*3,1*4,1*5,1*6,1*7,1*8,1*9,1*10)
    case 2:
        print(2 * 1, 2 * 2, 2 * 3, 2 * 4, 2 * 5, 2 * 6, 2 * 7, 2 * 8, 2 * 9, 2 * 10)
    case 3:
        print(3 * 1, 3 * 2, 3 * 3, 3 * 4, 3 * 5, 3 * 6, 3 * 7, 3 * 8, 3 * 9, 3 * 10)
    case 4:
        print(4 * 1, 4 * 2, 4 * 3, 4 * 4, 4 * 5, 4 * 6, 4 * 7, 4 * 8, 4 * 9, 4 * 10)
    case 5:
        print(5 * 1, 5 * 2, 5 * 3, 5 * 4, 5 * 5, 5 * 6, 5 * 7, 5 * 8, 5 * 9, 5 * 10)
    case 6:
        print(6 * 1, 6 * 2, 6 * 3, 6 * 4, 6 * 5, 6 * 6, 6 * 7, 6 * 8, 6 * 9, 6 * 10)
    case 7:
        print(7 * 1, 7 * 2, 7 * 3, 7 * 4, 7 * 5, 7 * 6, 7 * 7, 7 * 8, 7 * 9, 7 * 10)
    case 8:
        print(8 * 1, 8 * 2, 8 * 3, 8 * 4, 8 * 5, 8 * 6, 8 * 7, 8 * 8, 8 * 9, 8 * 10)
    case 9:
        print(9 * 1, 9 * 2, 9 * 3, 9 * 4, 9 * 5, 9 * 6, 9 * 7, 9 * 8, 9 * 9, 9 * 10)
    case 10:
        print(10 * 1, 10 * 2, 10 * 3, 10 * 4, 10 * 5, 10 * 6, 10 * 7, 10 * 8, 10 * 9, 10 * 10)
    case _:
        print("Not in the range.")


