#1.Напиши функцию calculate(a, b, operation) которая принимает два числа и строку "add", "sub", "mul", "div" и возвращает результат.

print("Hello Calculate")

def calculate(a, b, operation):
    if operation == "add":
        return a+b
    elif operation == "sub":
        return a-b
    elif operation == "mul":
        return a*b
    elif operation == "div":
        return a/b
    else:
        print("Please enter a valid operation")


a = int(input("Enter a number A: "))
b = int(input("Enter a number B: "))
operation = input("Enter operation(add,sub,mul,div): ")

result = calculate(a,b,operation)
print(result)