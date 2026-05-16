def calculator(num1,num2,operator):
    if operator == "+":
        return num1+num2
    elif operator == "-":
        return num1-num2
    elif operator == "*":
        return num1*num2
    elif operator == "/":
        return num1/num2
    else:
        return "wrong operator"

num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
operator = input("enter operator:")
result = calculator(num1,num2,operator)
print(result)