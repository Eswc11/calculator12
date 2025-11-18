# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# print(f"""
#     Max = {max(a,b)}
#     Min = {min(a,b)}
#     Median = {(a + b )/ 2}
# """)
import json
from calendar import month
from datetime import timedelta

# a = int(input("Enter number: "))
# if a >= 1000 and a <= 9999:
#     print(f"Число {a}")
#     print(*str(a), sep="\n")
#     # for i in str(a):
#     #     print(i)
#
# a = []
# for i in range(0,3):
#     num = int(input(f"Enter a number {i + 1}: "))
#     a.append(num)
# print(max(a) - min(a))


# a = int(input( " Enter the amount : "))
# b = a + 1
# if b > 1 and b % 2 == 0:
#     print(f'Amount : {b // 2}')
# elif b > 1 and b % 2 != 0:
#     print(f'Amount : {b}')
# else:
#     print("Гостей нет,Петя один")


# words = ['енот','слон','крокодил']
# a = []
# b = []
# c = []
# for i in range(0, 10):
#     num = int(input("Enter a data: "))
#     a.append(num)
#     num2 = int(input("Enter another data: "))
#     b.append(num2)
#     if len(a) == len(b):
#         f = a[i] + b[i]
#         c.append(f)
# print(a,b,c,max(c),min(c[-3:]))

# radiuses = [12,35,4]
# for i in radiuses:
#     squares = 3.14 * (i ** 2)
#     print(squares)
#
# age = int(input("Enter your age: "))
# a = age // 365
# b = a % 30
# c = (age % 365) % 30
# print(a,b,c)
# commands = ["list", "find", "add", "edit", "delete", "exit"]
#
# contacts = [
#     {
#         "name": "John",
#         "phone": "123456"
#     },
#     {
#         "name": "Jane",
#         "phone": "564321"
#     },
#     {
#         "name": "Bob",
#         "phone": "+1234"
#     },
# ]
# while True:
#     a = input("Choose action: ")
#     if a in commands:
#         if a == "list":
#             print(f"{'Имя':<10} {'Телефон':<10}")
#             for contact in contacts:
#                 print(f"{contact['name']:<10} {contact['phone']:<10}")
#         elif a == "find":
#             b = input("Enter name: ")
#             for contact in contacts:
#                 if b == contact['name']:
#                     print(f"Name found: {contact['name']} " + f" phone - {contact['phone']}")
#         elif a == "add":
#             b = input("Enter name: ")
#             c = input("Enter phone: ")
#             new_contact = {"name": b, "phone": c}
#             contacts.append(new_contact)
#             print(f"{'Имя':<10} {'Телефон':<10}")
#             for contact in contacts:
#                 print(f"{contact['name']:<10} {contact['phone']:<10}")
#         elif a == "edit":
#             b = input("Enter name: ")
#             for contact in contacts:
#                 if b == contact['name']:
#                     c = input("Enter new name: ")
#                     f = input("Enter new phone: ")
#                     contact["name"] = c
#                     contact["phone"] = f
#                     print(f"{'Имя':<10} {'Телефон':<10}")
#                     for contact in contacts:
#                         print(f"{contact['name']:<10} {contact['phone']:<10}")
#         elif a == "delete":
#             b = input("Enter name: ")
#             for contact in contacts:
#                 if b == contact['name']:
#                     contacts.remove(contact)
#                     print(f"{'Имя':<10} {'Телефон':<10}")
#                     for contact in contacts:
#                         print(f"{contact['name']:<10} {contact['phone']:<10}")
#         elif a == "exit":
#             print("Goodbye")
#             break
#         else:
#             print("Error")
#     else:
#         print("Error.Try again")
# from random import randint
# round = int(input("Enter a number of rounds: "))
# while True:
#     for i in range(round):
#         a = randint(1, 6)
#         b = randint(1, 6)
#         dice_sum = a + b
#         c = dice_sum - abs(a - b) * 2
#         cube1 = [[" "] * 3 for _ in range(3)]
#         cube2 = [[" "] * 3 for _ in range(3)]
#         choice = int(input("Enter number: "))
#         positions = {
#             1: [(1, 1)],
#             2: [(0, 0), (2, 2)],
#             3: [(0, 0), (1, 1), (2, 2)],
#             4: [(0, 0), (0, 2), (2, 0), (2, 2)],
#             5: [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)],
#             6: [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2)],
#         }
#         for x, y in positions[a]:
#             cube1[x][y] = "#"
#         for x, y in positions[b]:
#             cube2[x][y] = "#"
#         comp_x = randint(1, 6)
#         comp_y = randint(1, 6)
#         dice_comp = comp_x + comp_y
#         comp_c = dice_comp - abs(comp_x - comp_y) * 2
#         choice_comp = randint(2, 12)
#         cube3 = [[" "] * 3 for _ in range(3)]
#         cube4 = [[" "] * 3 for _ in range(3)]
#         for x, y in positions[comp_x]:
#             cube3[x][y] = "#"
#         for x, y in positions[comp_y]:
#             cube4[x][y] = "#"
#         if c > comp_c:
#             print("-" * 17)
#             for row1, row2 in zip(cube1, cube2):
#                 row_str1 = " ".join(row1)
#                 row_str2 = " ".join(row2)
#                 print(f"| {row_str1} | | {row_str2} |")
#             print("-" * 17)
#             print(f"On the dice fell {dice_sum} points.\n"
#                   f"Result is {dice_sum}-abs({dice_sum}-{choice})*2: {c} points")
#             print("-" * 17)
#             print(f"Computer predicted {choice_comp} points.\n")
#             for row3, row4 in zip(cube3, cube4):
#                 row_str3 = " ".join(row3)
#                 row_str4 = " ".join(row4)
#                 print(f"| {row_str3} | | {row_str4} |")
#             print("-" * 17)
#             print(f"Users win {c - comp_c} points more.")
#         elif c < comp_c:
#             print("-" * 17)
#             for row1, row2 in zip(cube1, cube2):
#                 row_str1 = " ".join(row1)
#                 row_str2 = " ".join(row2)
#                 print(f"| {row_str1} | | {row_str2} |")
#             print("-" * 17)
#             print(f"On the dice fell {dice_sum} points.\n"
#                   f"Result is {dice_sum}-abs({dice_sum}-{choice})*2: {c} points")
#             print("-" * 17)
#             print(f"Computer predicted {choice_comp} points.\n")
#             for row3, row4 in zip(cube3, cube4):
#                 row_str3 = " ".join(row3)
#                 row_str4 = " ".join(row4)
#                 print(f"| {row_str3} | | {row_str4} |")
#             print("-" * 17)
#             print(f"Computer win {comp_c - c} points more.")
#         elif c == comp_c:
#             print("-" * 17)
#             for row1, row2 in zip(cube1, cube2):
#                 row_str1 = " ".join(row1)
#                 row_str2 = " ".join(row2)
#                 print(f"| {row_str1} | | {row_str2} |")
#             print("-" * 17)
#             print(f"On the dice fell {dice_sum} points.\n"
#                   f"Result is {dice_sum}-abs({dice_sum}-{choice})*2: {c} points")
#             print("-" * 17)
#             print(f"Computer predicted {choice_comp} points.\n")
#             for row3, row4 in zip(cube3, cube4):
#                 row_str3 = " ".join(row3)
#                 row_str4 = " ".join(row4)
#                 print(f"| {row_str3} | | {row_str4} |")
#             print("-" * 17)
#             print(f"Draw {comp_c == c} points.")
#         else:
#             print("Try one more time.")
# a = [-1,2,3,-4]
# def change(a):
#     a = [-i for i in a]
#     print(a)
# change(a)
# def median():
#     a = list(map(int, input("Введите 10 чисел через пробел: ").split()))
#     med = sum(a) / len(a)
#     min_val = min(a)
#     max_val = max(a)
#     return med, min_val, max_val
# print(median())

# import random
#
#
# def check_random_distribution(num_samples):
#     groups = [0] * 10
#     for _ in range(num_samples):
#         rand_num = random.randint(0, 99)
#         group_index = rand_num // 10
#         groups[group_index] += 1
#
#     print("Number of samples:", num_samples)
#     for i in range(10):
#         start = i * 10
#         end = start + 9
#         print(f"Group {start}-{end}: {groups[i]}")
#
#
# check_random_distribution(100)
