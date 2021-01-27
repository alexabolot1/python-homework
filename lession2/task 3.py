"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

# решение через list

number_month = int(input("Введите номер месяца "))
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month = ['зима', 'весна', 'лето', 'осень']
if number_month == number[-1] or number_month == number[0] or number_month == number[1]:
    print(f'{number_month} месяц - это {month[0]}!')
elif number_month == number[2] or number_month == number[3] or number_month == number[4]:
    print(f'{number_month} месяц - это {month[1]}!')
elif number_month == number[5] or number_month == number[6] or number_month == number[7]:
    print(f'{number_month} месяц - это {month[2]}!')
elif number_month == number[8] or number_month == number[9] or number_month == number[10]:
    print(f'{number_month} месяц - это {month[3]}!')

# решение через dict

number_month = int(input('Введите номер месяца, и я подскажу какое это время года '))
month_dict = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
for key, value in month_dict.items():
    for val in value:
        if val == number_month:
            print(f'Итак, {number_month} месяц это {key}')
