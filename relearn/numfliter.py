def numfilter(numbers = []):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num*2)
    result.sort()
    return result


my_list = [5, 3, 8, 1, 12, 7, 4, 9, 6]
result = numfilter(my_list)
print(result)
