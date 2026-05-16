def longest_word(text):
    words = text.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

text = input("enter text:")
result = longest_word(text)
print(result)