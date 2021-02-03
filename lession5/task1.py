"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
 Об окончании ввода данных свидетельствует пустая строка.
"""
with open('task1.txt', 'w+', encoding='utf-8') as f_obj:
    while True:
        user_input = input('Введите какой-либо текст: ')
        if user_input == '':
            break
        else:
            f_obj.writelines(f'{user_input}\n')
    f_obj.seek(0)
    print(f_obj.read())
