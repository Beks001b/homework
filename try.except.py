#Exception - это объекты, который прерывают работу кода если они не обработаныи.
#Ошибки - объукты которые прерывают аботу кода но их нельзя обработать не считая исключения

IndexError
# это исключение который выходит когда мы обращаемся по несуществующему индексу 

'''
list_1 = [23, 15, 4, 2]
list_1[1000]
'list index out of range'
'''

'''
list_2 = [12,23,2,1]
list_2.pop(1000)
'pop index out of range'
'''

'''
list_3 = []
list_3.pop()
pop from empty list
'''

KeyError
# исключение который выходит когда обращаемся по несуществуещему ключу

'''
dict1 = {'a':1}
dict1['b']
KeyError: 'b'
'''

ValueError
# когда мы передаем в фуккцию не корекный для нее тип данных
# когда мы распаковываем итерируемый обьект на несколько переменных,
# кол-во переменных не совпадает с кол-вом элементов в итерируемый обьект

'''
int('10d')
ValueError: invalid literal for int() with base 10: '10d'
'''

'''
a, b, c = [1,2,3,4]
print(b)
ValueError: too many values to unpack (expected 3)
'''

TypeError
#когда мы пытаемся использовать метод не свойственный какоку-то типу данных
#2 когда мы пытаемся передать функции выше или меньше аргументов чем принимает функция 

'''
for i in 12345678:
    ...
TypeError: 'int' object is not iterable
'''

'''
5 + '5'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''

'''
'5' + 5 
TypeError: can only concatenate str (not "int") to str
'''

'''
{[1,2,3]:'hello'}
TypeError: unhashable type: 'list'
'''

'''
input('enter, 2')
 '''

''' 
list1 = []
list1.append()
TypeError: list.append() takes exactly one argument (0 given)
'''

ZeroDivisionError
#выходит при делении на 0

'''
45 // 0
ZeroDivisionError: integer division or modulo by zero
'''

'''
3 % 0 
ZeroDivisionError: integer division or modulo by zero
'''

AttributeError
# выходит когда мы обращаемся к несуществующему аттребуту или методу обьекта (типа данных)

'''
[].replace('', 'a')
AttributeError: 'list' object has no attribute 'replace'
'''

'''
''.pop()
AttributeError: 'str' object has no attribute 'pop'
'''

SyntaxError
'''
my num = 50 
SyntaxError: invalid syntax
a = 
'''

IndentationError
# исключение которые выходит когда мы используем не правильный отступ
'''
    num = 15
IndentationError: unexpected indent
'''

'''
for i in range(11):
print(i)
IndentationError: expected an indented block after 'for' statement on line 125
'''

NameError
'''
# исключение которое выходит когда обращаемся к несуществующей ппеременной 
num1 = 15
print(num2)
NameError: name 'num2' is not defined. Did you mean: 'num1'?
'''

#Вызов исключений
# raise NameError('я вызвал тебя')

Exception
#исклюючение которые создали чтобы его вызывать (родитель)

#чтобы код не пркращал свою работу мы можем использовать конструкцию
#try-except и обрабатывать вызванное исключение

# count = 0
# while count == 0:
# try:
#     # код который возможно вызовит ошибку
#     num = int(input('введите число'))
# except ValueError:
#     #код который обрабатывает только если ошибка вызвалась
#     print('Вы ввели не число')
# else:
#     # пишется код который отрабатывает только если никакая ошибка не вышла
#  print('вы ввели число')
#  break
# finally:
#     #Сработает в любом случаи 
# print('пока')
    
# try:
#     raise NameError
# except (ArithmeticError, ValueError):
#     print('вышла ошибка - atreburerror или в valueerror')
    
    
# try:
#     raise ZeroDivisionError
# except:
#     print('hi')
    
# try:
#     raise ZeroDivisionError
# except Exception:
#     print('hi')
    
    
# try:
#     raise ValueError
# except  ValueError:
#     print('вышел valuerror')
# except TypeError:
#     print('вышел typerror')
    
# try:
#     print(11)
# finally:
#     print('hi')

'============================Comprehension=============================================='
# это генератор с помощью которого мы можем создать последовательность используя цикд for в одну строку 

#элемент for переменная in последовательность
#элемент for переменная in последовательность if условие
#элемент if  условие else элемент2 for переменная in последовательность
# элемент if условие else элемент2 for переменная in последовательность if фильтр

'3 вида генератора'
list
set
dict

# comp = (i**2 for i in range(11) if i % 2 == 0)
# print(comp)
# # print(list(comp))
# print(set(comp))

# list1 = [-12, 93, 0, 4, -1]
# list2 =['+' if i >=0 else '-' for i in list1]
# print(list2)


# [1,2,3,45,4]
# [нечетный четный нечетный нечетный ]

# {'a':1, 'b':2
# {1:'a', 2:'b'}

# list = [1, 2, 4, 67]
# list2 = ['четный' if i %2 ==0 else 'нечетный' for i in list ]
# print = (list2)


# for i in (1,2,33):
#     if i % 2 == 0:
#         print(f'{i} - четное')
#     else:
#         print(f'{i} - нечетное')
        
# # Проходим по диапазону от 1 до 10
# for number in range(1, 11):
#     if number % 2 == 0:  # Проверка на четность (остаток от деления на 2 == 0)
#         print(f"{number} - четное")
#     else:
#         print(f"{number} - нечетное")


