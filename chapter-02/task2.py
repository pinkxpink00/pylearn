#2.Напиши программу которая выводит числа от 1 до 20, но вместо чисел кратных 3 пишет Fizz, кратных 5 — Buzz, кратных обоим — FizzBuzz.

for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)