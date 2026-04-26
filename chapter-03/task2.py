#2.Напиши функцию generate_password(length) которая генерирует случайный пароль из букв и цифр заданной длины. Используй random и string модули.

import secrets
import string
import random


def generate_password(length):
    allowed_chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(allowed_chars) for i in range(length))
    return (password)

print(generate_password(8))