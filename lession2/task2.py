"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

"""

list_one = []
list_two = []
item_number = 0
while True:
    a = input('Введите любой элемент (число, букву, символ, слово и т.д.)')
    if a == '':
        print('Формирование первого списка окончено')
        break
    else:
        list_one.append(a)
print(list_one)
while True:
    if len(list_one) != 1:
        list_two.append(list_one[item_number + 1])
        list_two.append(list_one[item_number])
        item_number += 2
        if item_number >= len(list_one) - 1:
            break
    else:
        break
if len(list_one) % 2 != 0:
    list_two.append(list_one[-1])
print(list_two)
