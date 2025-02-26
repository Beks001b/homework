'=====================set==========================================='
# set - изменяемый неупорядочный индуксируемый итерируемый тип данных который хранит в себе
#уникальные значение так же только элементы которые являются неизменяемый типами данных  

# set1 = {1,2,3,1,False}
# print(set1)
# print(dir(set))

# for i in set:
#     print(i)
    
# tuple = 12,
# print(type(tuple))

# print(dir(tuple))

# tuple1 = (1,2,3)
# tuple2 = (1,2,5)
# print(id(tuple1))
# print(id(tuple2))

# list1 = [1,2,3,4,5,6,1,2,3]
# set1 = set(list1)
# list2 = list(set1)
# print(list2)

'================================функции========================================='
#функции - именнованный блок кода который может принимать аргументы и возврощать результаты
# def my_sum(x, y): #x , y = параментры 
#     return x + y 
# res = my_sum(5, 2) # 5, 2 = аргументы 
# print(res)

# res2 = my_sum(10, 23)
# print(res2)

# def my_len(posl):
#     count = 0
#     for i in posl:
#         count += 1
#     return count

# res1 = my_len([34,1,34,2,2])# 5
# res2 = my_len('hello world')# 11
# res3 = my_len({12,2,32,2,12,1})# 4
# print(my_len)

'==================================Виды парамента============================================='
#1. обязательные
#2. необязательные
#3. с дефолдом(со значением по умолчанию)
#4. *args - все позиционные аргументы которые не попали в обязательные и с дефолдом
#5. **kwargs - все лишние именнованные аргументы


# def func(x=1, y=1, z=6):
#     return x + y + z

# print(func(10,5))

'=========================================Виды аргументов=================================='
#1 позиционные (по позиции)
#2 именнованные (по названию
# параметр=фргументы)

# def add_or_add_10(num1, num2=10):
#     return num1 + num2

# print(add_or_add_10(5,2)) #7
# print(add_or_add_10(40)) #50

# def func(a,b=10, *args, **kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)
    
# func(10)
# func(20,30)# позиционные
# func(b=30,a=40)#именнованные нужны для **kwargs
# func(40,50,60,70,80)
# func(40,50,60,70, hello='hello world', hi='hi')

'===========================lambda===================================='
#lambda - это ананонимная функция которая записывается в одну строку 
# lambda_func = lambda x, y: x ** y
# print(lambda_func(5, 2))

# def func(x):
#    return x ** 3
# print(func(5))

# users = [
#     {'username':'katana', 'password1':'205221', 'password2':'205221'},
#     {'username':'Uraimov00' , 'password1':'QAZqwe123', 'password1':'QAZqwe123'}
# ]
# def voiti():
#     if action == '2':
#         username = input('username: ')
#         for user in users:
#             if user['username'] == username:
#                 password = input('password: ')
#                 for user in users:
#                     if user['username'] == password:
#                         break
#         else:
#             print('такого пользователя нет')
            
# def registr():
#         username = input('username: ')
#         password = input('password: ')
#         password2 = input('повторите пароль: ')
#         user = {
#             'username': username,
#             'password': password,
#             'pasword2': password2
#         }
#         users.append(user)
        
        
        
        
# users = [
#     {'username': 'katana', 'password1': '205221', 'password2': '205221'},
#     {'username': 'Uraimov00', 'password1': 'QAZqwe123', 'password2': 'QAZqwe123'}
# ]

# def voiti():
#     username = input('Введите username: ')
#     for user in users:
#         if user['username'] == username:
#             password = input('Введите пароль: ')
#             if user['password1'] == password:
#                 print("Успешный вход!")
#                 return
#             else:
#                 print("Неверный пароль!")
#                 return
#     print('Такого пользователя нет!')

# def registr():
#     username = input('Введите username: ')
#     password = input('Введите пароль: ')
#     password2 = input('Повторите пароль: ')

#     if password != password2:
#         print("Пароли не совпадают!")
#         return

#     for user in users:
#         if user['username'] == username:
#             print("Такой пользователь уже существует!")
#             return

#     users.append({'username': username, 'password1': password, 'password2': password2})
#     print("Регистрация успешна!")

# while True:
#     action = input('Выберите действие: 1. Регистрация, 2. Логин, 3. Выход: ')
#     if action == '1':
#         registr()
#     elif action == '2':
#         voiti()
#     elif action == '3':
#         print("Выход...")
#         break
#     else:
#         print("Неверный ввод, попробуйте снова.")
        
def munu():
    chois = input('Что вы хотите сделать ?.1.Войти.2.зарегться')
    return chois

users ={'username': 'katana', 'password1': '205221', 'password2': '205221'},
{'username': 'Uraimov00', 'password1': 'QAZqwe123', 'password2': 'QAZqwe123'}
    
def register(users):
    username = input('Введите username')
    password1 = input('введите password')
    password2 = input('подтвердите password')
    users.append[{'username':username, 'password1':password1, 'password1':password2}]
    print('вы успешно зарегались')
    
def voiti(users):
    username = input('Введите логин: ')
    for user in users:
        if user['username'] == username:
            password = input('Введите пароль')
            if password ==user['password1']:
                print('Вы успешно вошли')
            else:
                print('Неверный пароль')
                break
        else:
            print('Такого нет')
            
chois = munu()
if chois == '1':
    voiti(users)
elif chois == '2':
    register(users)
        



