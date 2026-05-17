#Задача 1 — Простая
#Создай словарь с данными о себе (имя, возраст, город, email). Выведи всё в формате ключ: значение через цикл .items().

person = {"name": "German", "age": 26, "city": "Cherkasy", "email": "kyperu07@gmail.com"}

for key, value in person.items():
    print(key, value)