def countchar(text):
    letters = 0
    digits = 0
    spaces = 0
    for char in text:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        else:
            print(char)

    print(f"Букв: {letters}")
    print(f"Цифр: {digits}")
    print(f"Пробелов: {spaces}")

text = input("enter text:")
countchar(text)
