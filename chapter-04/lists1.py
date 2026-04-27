#Список — это коллекция элементов в определённом порядке. Как массив в C#, но гибче — можно хранить разные типы данных в одном списке.

#Создание
fruits = ["apple", "banana", "cherry"]

#Доступ по индексу
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1])

#Срез
print(fruits[0:3])
print(fruits[1:])

#Длинна
print(len(fruits))


#Добавление
fruits.append("mango")
print(fruits)
fruits.insert(1, "orange")
print(fruits)

#Удаление
fruits.remove("orange")
print(fruits)
fruits.pop()
print(fruits)
fruits.pop(2)
print(fruits)

#Полезности
numbers = [1,5,67,8,4,2,5,6,7,89,100]
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.reverse()
print(numbers)
print(numbers.count(5))
print(numbers.count("apple"))
print(numbers.index(100))