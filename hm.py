# import random

# def draw_dice(n):
#     faces = {
#         1: ("┌─────┐", "│     │", "│  ●  │", "│     │", "└─────┘"),
#         2: ("┌─────┐", "│ ●   │", "│     │", "│   ● │", "└─────┘"),
#         3: ("┌─────┐", "│ ●   │", "│  ●  │", "│   ● │", "└─────┘"),
#         4: ("┌─────┐", "│ ● ● │", "│     │", "│ ● ● │", "└─────┘"),
#         5: ("┌─────┐", "│ ● ● │", "│  ●  │", "│ ● ● │", "└─────┘"),
#         6: ("┌─────┐", "│ ● ● │", "│ ● ● │", "│ ● ● │", "└─────┘"),
#     }
#     return faces[n]

# def get_number():
#     while True:
#         try:
#             n = int(input("Загадайте число от 2 до 12: "))
#             if 2 <= n <= 12:
#                 return n
#         except ValueError:
#             pass
#         print("Ошибка! Введите число от 2 до 12.")

# y = get_number()
# input("Нажмите Enter, чтобы бросить кости...")

# d1, d2 = random.randint(1, 6), random.randint(1, 6)
# x = d1 + d2

# for line1, line2 in zip(draw_dice(d1), draw_dice(d2)):
#     print(line1, line2)

# score = x - abs(x - y) * 2
# print(f"\nНа кубиках выпало: {x}")
# print(f"Формула: {x} - |{x} - {y}| * 2 = {score}")
# print("Вы выиграли!" if score > 0 else "Вы проиграли!")



