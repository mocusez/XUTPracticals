MENU = """E - Show the even numbers from x to y
O - Show the odd numbers from x to y
S - Show the squares from x to y
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "E":
        print("Input the number X and Y")
        x, y = input().split()
        x = int(x)
        y = int(y)
        # print even
        if x%2 == 0:
            for i in range(x,y,2):
                print(i,end=' ')
            if(y % 2 == 0):
                print(y)
        else:
            x = x+1
            for i in range(x, y, 2):
                print(i,end=' ')
            if (y % 2 != 0):
                print(y)

    elif choice == "O":
        print("Input the number X and Y")
        x, y = input().split()
        x = int(x)
        y = int(y)
        # print Odd
        if x%2 != 0:
            for i in range(x,y,2):
                print(i,end=' ')
            if(y % 2 == 0):
                print(y)

        else:
            x = x+1
            for i in range(x, y, 2):
                print(i,end=' ')
            if (y % 2 != 0):
                print(y)

    elif choice == "S":
        for i in range(x, y, 1):
            print(i**0.5)