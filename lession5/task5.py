"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open('task5.txt', 'w+', encoding='utf-8') as f_obj:
    numbers = '255 10 147 96 55 2 73'
    f_obj.writelines(numbers)
    f_obj.seek(0)
    numbers = [int(numb) for numb in f_obj.readline().split()]
    print(f'Сумма всех введённых вами чисел равна: {sum(numbers)}')
