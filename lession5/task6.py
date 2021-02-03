"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не
обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество
 занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def my_func(string):
    try:
        number = ''
        for i in string:
            if i.isdigit() is True:
                number += i
        number = int(number)
        return number
    except ValueError:
        return 0


my_dict = {}
with open('task6.txt', encoding='utf-8') as f_obj:
    for line in f_obj:
        subject, lecture, practice, lab = line.split()
        my_dict[subject] = my_func(lecture) + my_func(practice) + my_func(lab)
    print(my_dict)
