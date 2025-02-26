# dick(Словари) - это изменяемый интерируемый неупорядочный 'неиндексируемый' тип данных для хранение данных в парах (ключь:значение)

# user = {
#     'name':'bek',
#     'age':21,
#     'prof':'dev'
# }

# print(user['name'])
# print(user['age'])

# ключами в словаре могут быть только не изменяемые типы данных
# если в словаре есть одинакоые ключи то сохроняется последняя

# создание 
# dict = {'a':1, 'b':2}
# list1 = [[1, 'a'], [2, 'b'], [3, 'c']]
# list2 = []
# dict2 = dict(list1)
# print(dict)

# dick1 = {'c':3}
# dick1['a'] = 1 
# dick1['b'] = 2
# print(dick1)

# методы словарей (get) - метод который возврощает значение по ключу если такого нет то возврощает None или дефолтное значение
# user = {
#     'name':'bek',
#     'age':21,
#     'prof':'mentor'
# }
# print(user.get(input('enter: ')))


# pop - удаляет пару по ключу и возврощает значение
# dict = {
#     'a':1,
#     'b':2
#}
# poped_values = dict.pop('b')
# print(poped_values)


# popitem - удаляет последнюю пару и возврощает ее 
# dict = {
#     'a':1,
#     'b':2
# }
# poped_items = dict.popitem()
# print(poped_items)

#update - расширает словарь парами из второго словаря 
# dict = {1;'a', 2:'a'}
# dict2 = {3;'a', 4:'a'}
# dict.update(dict2)
# print(dict)