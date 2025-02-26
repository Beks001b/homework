'=========================функции высшего порядка========================================'
# функции высшего порядка - это  функции которые принимают в аргументы другую функцию либо
#создает внутри себя вызывает функцию и возврощает функцию
# def func(x):
#     ...
    
# def func_2():
#     ...
    

# func(func_2)

# def func_1():
#     ...
#     def func_2():
#         ...

        
# def func_1():
#     ...
    
# def func_2():
#     func_1()

# def func1():
#     print('hi')
#     return func1
# print(func1()()())

'=====================декораторы=============================='
# Декоратор это функци высшего порядка которая нужна чтобы расширить функционал другой 
#функции не изменяя ее (функции оберток)

     
# def glush(x):
#     def wrapper (*args, **krwegs):
#         print('Тихо')
#         x()
#     return wrapper

# @glush
# def pistolen():
#     print('стрелять')
    
# @glush
# def avtomat():
#     print('стрелять')

# pistolen()
# avtomat()
# glush(pistolen)()
# glush(avtomat)()


# def a(func):
#     def b(*args, **kwargs):
#         print('Выполнение функции')
#         return func(*args, **kwargs)
#     return b

# @a
# def c():
#     print('Завершение функции')

# c()


# def print_before(func):
#     def wrapper(*args, **kwargs):
#         print("Выполнение функции...")
#         return func(*args, **kwargs)
#     return wrapper

# # Пример использования декоратора
# @print_before
# def some_function():
#     print("Функция выполнена!")

# # Вызов функции
# some_function()


# def a(func):
#     def wrapper(*args, **kwargs):
#         print('Функция начинает работать')
#         result = func(*args, **kwargs)
#         print('Функция стоп')
#         return result
#     return wrapper


# @a
# def c():
#     print('Фунция выполняется')
    
# c()

# def a(fuck):
#     def b(*args, **kwargs):
#         print('привет') 
#         reult = fuck(*args, **kwargs)
#         return reult
#     return b
# @a
# def c():
#     print('Функция выполнена')
    
# c()


# def a(func):
#     def b(*args, **kwargs):
#         print('Начало выполнения')
#         res = func(*args, **kwargs)
#         print('Конец функции')
#         return res 
#     return b

# @a
# def c():
#     print('Функция выполняется')
    
# c()

