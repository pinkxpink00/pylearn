#Напиши функцию caesar_cipher(text, shift) которая шифрует текст методом Цезаря — каждая буква сдвигается на shift позиций в алфавите.
#Это кстати реальная тема из криптографии в CTF.

later = 'A'
shift = 3
new = chr(ord(later)+shift)
print(new)



text = "hello world"
shift = 3
result = ""

for char in text:
    new = chr(ord(char)+shift)
    result = result + new

print(result)


def ceaser_cipher(text,shift):
    result = ""
    for char in text:
        if char == " ":
            result = result + " "
        else:
            new = chr(ord(char)+shift)
            result = result + new
    return result


text = input("input text in ceaser cipher: ")
shift = int(input("input shift in ceaser cipher: "))
print(ceaser_cipher(text,shift))