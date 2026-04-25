#1.Напиши программу которая спрашивает число и выводит чётное оно или нечётное.

number = int(input("enter a number"))

if number % 2 == 0:
    print("even number")
else:
    print("odd number")