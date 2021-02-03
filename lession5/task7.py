"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json
final_list = []
firm_dict = {}
average_dict = {'средняя прибыль': None}
profit_sum = 0
profit_firm = 0
with open('task7.txt', encoding='utf-8') as f:
    for i in f.readlines():
        firm = i.split()
        profit = int(firm[2]) - int(firm[3])
        if profit > 0:
            profit_sum += profit
            profit_firm += 1
        average_dict['средняя прибыль'] = profit_sum // profit_firm
        firm_dict[firm[0]] = profit
final_list.append(firm_dict)
final_list.append(average_dict)
print(final_list)

with open('task7.json', 'w+', encoding='utf-8') as write_file:
    json.dump(final_list, write_file, ensure_ascii=False)
