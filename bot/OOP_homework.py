class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Пополнено: {amount}')
        else:
            print('Пополнение должно быть больше 0')

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f'Снято: {amount}')
        else:
            print('Недостаточно средств')

    def get_balance(self):
        return self.__balance


account = BankAccount()
account.deposit(1000)
account.withdraw(10000)
print("Текущий баланс:", account.get_balance())
account.withdraw(600)
print("Баланс после снятия:", account.get_balance())
'================================================================'
class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = None
        self.set_password(password)

    def get_password(self):
        if self.__password:
            return '*' * len(self.__password)
        return None

    def set_password(self, new_password):
        if len(new_password) > 6 and new_password.isalnum():
            self.__password = new_password
            print("Пароль установлен.")
        else:
            print("Ошибка:Пароль должен быть длиннее 6 символов и содержать только буквы и цифры.")
'============================================================='
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = None
        self.salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value >= 30_000:
            self.__salary = value
            print("Зарплата установлена")
        else:
            print("Ошибка:зарплата не может быть меньше 30 000.")
'====================================================================================='



        