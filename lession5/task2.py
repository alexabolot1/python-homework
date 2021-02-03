"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
 количества слов в каждой строке.
"""
f_obj = open('task2.txt', encoding='utf-8')
lines = 0
for lin, content in enumerate(f_obj.readlines(), 1):
    lines = lin
    print(f'В строке под номером {lin} находятся слова в количестве {len(content.split())}.')
print(f'Строк в вашем файле - {lines}.')
