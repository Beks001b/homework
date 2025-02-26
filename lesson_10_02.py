'==================================Встроенные функции========================'
#map, fillter, reduce, zip, enumerate

#zip - соединяет несколько последовательностей (получаем генератор , 
# в котором элементы - tuple)

# list1 = [1,2,3,4]
# list2 = ['a', 'b', 'c', 'd']
# list3 = [0.1, 5.5, 10.8, 1.1]

# zipped = zip(list1, list2)
# print(set(zipped))
# for i in zipped:
#     print(i)

# enumerate - нуммерует последовательность 
#(по дефолду с 0) (тоже получает генератор)
# a = enumerate('hello', 10)
# print(list(a)) # обьязательно надо превращять либо в лист или dick 

# for num, elem in a:
#     print(num, elem)
    
    
# map - Принимает другую функцию и последовательность(записывает в новую последовательность результат 
# функции, в которую передаются элементы последовательность)

# list1 = ['1', '3', '3', '4']
# a = map(int, list1)
# print(list(a))

# def func(x):
#     return x ** 2

# list1 = [1,2,3,4]
# m = list(map(func, list1))
# print(m)

# print(list(map(lambda x: x ** 2, [1,2,3])))


# filter - возврощает генератор с элементами прошедшами фидьтрацию
# (какое - то усдовие) принимает функйию и последовательность


# list1 = ['hello', 'hi', '123', '3']
# a = filter(str.isdigit, list1) #isdigit - Для проверки цифер в строчной фигне
# print(list(a))

# print(list(filter(lambda x: x > 0, [23, -3, 2, -5])))

'=====================reduse======================='
# reduce - принимает функцию и последовательность, возвращает 1 результат (передаваемая функция должна принимать 2 аргумента)

# from functools import reduce

# print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))

# from functools import reduse
# print(reduse(lambda x, y:x + y, [1,2,3,4]))
'================================================================'
'zip'
# list1 = [1, 2, 3, 4, 5]  
# list2 = [1, 3, 3, 0, 5]
# zipped = list(zip(list1, list2))
# print(list(map(lambda x: x[0] == x[1], zipped)))
# print(list(map(lambda x: x[0] == x[1] , zip(list1, list2))))
'filtre'
# print(list(filter(lambda x: len(x) > 5, ['hi', 'hello', 'master'])))
# print(list(filter(lambda x: x[0] in 'аеёюияуоэ', ['яблоко','hello'])))
# print(list(filter(lambda x:x == x[::-1], ['heleh', 'olo', 'hello', 'bomba'])))
'reduse'
# list1 = [1,4,5,6]
# from functools import reduce
# print(reduce(lambda x:x + ))
# from functools import reduce
# print(reduce(lambda x,y: x * y, [12, 2, 3,4] ))