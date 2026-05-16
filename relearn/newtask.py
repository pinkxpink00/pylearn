def numbersss(num1):
    #чётное или нечётное
    if num1 % 2 == 0:
        print("чётное")
    else:
        print("нечётное")
    #знак
    if num1 == 0:
        print("num is 0")
    elif num1 > 0:
        print("num is positive")
    elif num1 < 0:
        print("num is negative")

    digits = len(str(abs(num1)))
    print(digits)

num1 = int(input("enter num1:"))
numbersss(num1)