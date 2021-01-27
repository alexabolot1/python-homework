"""
 Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
  Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара
   и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
    Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
 например название, а значение — список значений-характеристик, например список названий товаров.

"""

products = []
# переменная для хранения списка словарей
user_list = []
# переменная для хранения заключительного списка кортежей
a = int(input('Введите количество желаемых товаров '))
keys = ['название', 'цена', 'количество', 'единицы измерения']
val = []
# переменная для хранения списка вводимых пользователем значений
while len(products) != a:
    for i in keys:
        val.append(input(f'Введите {i} товара '))
    dict_one = dict(zip(keys, val))
    products.append(dict_one)
    val.clear()
for i in enumerate(products, 1):
    user_list.append(i)
user_dict = {
    'название': [],
    'цена': [],
    'количество': [],
    'единицы измерения': set()
}
for i in products:
    user_dict['название'].append(i['название'])
    user_dict['цена'].append(i['цена'])
    user_dict['количество'].append(i['количество'])
    user_dict['единицы измерения'].add(i['единицы измерения'])
print(user_dict)
