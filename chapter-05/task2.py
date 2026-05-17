#Напиши функцию count_words(text) которая принимает строку и возвращает словарь где ключ — это слово, а значение — сколько раз оно встречается в тексте
#count_words("hello world hello python world hello")
# {'hello': 3, 'world': 2, 'python': 1}


def count_words(text):
    count = {}
    sentences = text.split()
    for sentence in sentences:
        if sentence in count:
            count[sentence] += 1
        else:
            count[sentence] = 1

    return count

print(count_words("hello world hello python world hello"))