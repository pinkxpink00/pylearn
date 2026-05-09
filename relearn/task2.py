def task2():
    print("Задача2: Калькулятор")
    num1 = int(input("enter num1:"))
    num2 = int(input("enter num2:"))
    operator = input("enter operator +-*/:")

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    else:
        print("неккоректный ввод")

task2()