'===========================Области видимости==============================='
# LEGB - Local enclosed gljbal build-in 

'==============================Build-in==============================='
#Это всроенная пространство имен (list, print, input, str, set, len)

'===============================Global================================'
# пространтсво в файле в котором мы пишем код 
# globals() = это функция которая показывает переменные и функции внутри глобального пространство (в файле)
# num1 = 25 # global
# str = 'hello' 
# print(globals())


'========================LOCAL==============================='
# Локальная пространство - пространство которое находится внтури функции 
# var = 'global'
# def func():# global
#     num = 120 # local
#     num2 = 45 # local
#     str = 'sss' # local
# print(globals())

# var = 'global'
# def func():
#     var = 'local'
#     print(var)
# print(var)
# # print(var)
# func()

'================================Enclosed=========================='
# замкнутое пространство - которая является логальным у которого есть внутри локальная пространство
# var = 'global'
# def func():
#     var = 'local'#encloused
    
#     def inner_func():
#         var = 'local'
        
# print(var)
# func()


# def func():
#     a = 'local' 

# print(a)
# глобфльное пространство не видит переменные из локального пространства 

# count = 1

# def in_count():
#     global count
#     print(count)
#     count += 1
    
# in_count() # 1
# in_count() # 2
# in_count() # 3

# def count(i):
#     counter = 0
    
#     def in_counter():
#         nonlocal counter
#         print(counter) 
#         counter = counter + 1
        
#         for elem in range(i):
#             in_counter()
# count(5)

# def a():
#     b = float(input('Введите число: '))
#     c = float(input('Введите число 2: '))
#     op = input('Введите значение: ')
#     D = {
#         '+':b + c,
#         '-':b - c,
#         '*':b * c,
#         '/':b / c
#     }
#     result = D.get(op)
#     print(f'Результат: {result}')
# a()

# def a():
#     num1 = float(input('Введите число: '))
#     num2 = float(input('Введите число2: '))
#     op = input('Введите значение: ')
#     q = {
#     '+':num1 + num2,
#     '-':num1 - num2,
#     '*':num1 * num2,
#     '/':num1 / num2
#     }
#     result = q.get(op)
#     print(f'Результат: {result}')
# a()

# def a():
#     b = input('Ваше имя: ')
#     c = int(input('Введите возвраст: '))
#     if c < 18:
#         print('Ты еще подросток!!!')
#     elif c > 18:
#         print('Ты уже взрослый!!!')
#         print(f'Привет {b}', f'Тебе:{c} лет')
#         print('Ты уже взрослый')

# a()
# def a():
#     login = input('Введите логин: ')
#     password = input('Введите пароль: ')
#     if (len(password) >= 8 and
#     any(char.isdigit() for char in password) and
#     any(char.isupper() for char in password) and
#     any(char.islower() for char in password)):
#      print("Пароль успешно сохранён!")
#     else:
#      print("Пароль слишком слабый!")
# a()

import random

def gues_number():
    s_number = random.randint (1, 100)
    popytki = 0
    print('Я загадал число попробуй угадать')
    while True:
        try:
            number = int(input('Загадайте число: '))
            popytki += 1
            if number < s_number:
                print('Загадай число больше')
            elif number > s_number:
                print('Загадай число меньше')
            else:
                print(f'Вы угадали число {s_number} за {popytki} попытки')
                break
        except ValueError:
            print('Введите целое число')
gues_number()