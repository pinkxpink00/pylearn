#Функция — это блок кода с именем, который можно вызвать много раз. Пишешь один раз — используешь везде.

def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3, 4, 5)

def greet(**kwargs):
    print(kwargs)

greet(name="German", age=20)


def greetings(age,name,greeting = "hello"):
    print(f"{greeting},{name},{age}")

greetings(25,"German")