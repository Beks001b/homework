def a(func):
    def b(*args, **kwargs):
        print('выполнение функции')
        res = func(*args, **kwargs)
        return res
    return b
@a
def c():
    print('конец')
c()

def a(func):
    return lambda *args, **kwargs: func(*args, **kwargs) *2
@a
def b(a,b):
    return a + b
print(b(5, 5))


def a(func):
    return lambda *args, **kwargs:func(*args, **kwargs) + '!'
@a
def c(name):
    return(f'привет,{name}')
print(c('Бек'))

def a(func):
    def wrapper(*args, **kwargs):
        wrapper.b += 1
        if wrapper.b > 3:
            print("Функция больше недоступна")
            return
        return func(*args, **kwargs)
    wrapper.b = 0
    return wrapper

@a
def my_function():
    print("Функция выполнена")

my_function()  
my_function()  
my_function()  
my_function()  


def print_args(func):
    def wrapper(*args, **kwargs):
        print(f"Аргументы: {args}, Ключевые аргументы: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@print_args
def greet(name, age):
    print(f"Привет, {name}, тебе {age} лет!")

# Пример вызова
greet("Алексей", 30)



