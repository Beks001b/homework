# 1 задание
# try:
#     ...
# except:
#     ...
# else:
#     ...
# finally:
#     ...
# 2 задание
# try:
#     print(aaa)
# except Exception:
#     print('такой переменной не сушествует')
# 3 задание
# try:
#     num1 = float(input('Введите число: '))
#     num2 = float(input('Введите 2 число: '))
#     res = num1 / num2
# except ZeroDivisionError:
#     print('на ноль делить нельзя')
# except ValueError:
#     print('введите число')
# else:
#     print(res)
# 4 задание
# try:
#     num1 = int(input('введите число: '))
#     num2 = int(input('введите 2 число: '))
#     res = num1 + num2
# except ValueError:
#     print('Введите цифры')
# else:
#     print(res)
# 5 задание
# try:
#     my_dick = {'a':1, 'b':2}
#     key = input('введите ключ: ')
#     print(my_dick[key])
# except KeyError:
#     print('такого ключя не существует')
# else:
#     print('значение по ключу ')

# 6 задание
# str1 = 'Hello'
# print(str1[0])

# 7 задание
# try:
#     a = int(input('Введите возраст: '))
#     if a <18:
#         print('нельзя тебе')
# except ValueError:
#     print('Введен некоректный возраст')
# else:
#     print('спасибо')
# finally:
#     print('До свидание')

# 8 задание
# try:
#     num1 = int(input('Введите число: '))
#     num2 = int(input('Введите 2 число: '))
# except ValueError:
#     print('Введите цифры')
# except ZeroDivisionError:
#     print('Нельзя делить на 0')
# else:
#     print(num1 / num2)

# 9 задание
# try:
#     amount = float(input("Введите сумму денег: "))
#     if amount < 0:
#         raise ValueError("Сумма не может быть отрицательной!")

# except ValueError as e:
#     print(f"Ошибка: {e}")

# else:
#     print(f"Введенная сумма: {amount}")

# 10 задание
# try:
#     string = input("Введите строку: ")
#     number = float(input("Введите число: ")) 
#     result = string + number

# except TypeError:
#     print("Unsupported option")

# else:
#     print("Результат:", result)

