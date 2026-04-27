#Напиши функцию remove_duplicates(lst) которая принимает список с повторяющимися элементами и возвращает список без дубликатов, сохраняя порядок.

def remove_duplicates(lst):
    lst = set(lst)
    lst = list(lst)
    return lst

print(remove_duplicates([1, 2, 1, 1, 2, 4, 5, 6]))

