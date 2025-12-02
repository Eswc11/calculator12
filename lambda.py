# a = [1,2,3,6,5,4]
# def sort(numbers: list[int],is_reversed:bool=False):
#     if is_reversed == False:
#         for i in range(len(numbers)):
#             for j in range(i + 1,len(numbers)):
#                 if numbers[i] > numbers[j]:
#                     numbers[i],numbers[j] = numbers[j],numbers[i]
#     else:
#         for i in range(len(numbers)):
#             for j in range(i + 1,len(numbers)):
#                 if numbers[i] < numbers[j]:
#                     numbers[i],numbers[j] = numbers[j],numbers[i]
# sort(a)
# print(a)
# users = {
#     'John': 500,
#     'Sam': 5875,
#     'Dave': 560,
#     'Cat': 400,
#     'Jack': 5874,
#     'Michael': 20
# }
# def return_user(users):
#     a = sorted(users.items(), key=lambda x: x[1], reverse=True)
#     b = [user[0] for user in a[:3]]
#     return b
# print(return_user(users))
from Tools.scripts.dutree import display
from unicodedata import digit


# print(list(map(int,input("Введите цифры через запятую: ").split(","))))
# nums = [45,90,44,37,95,50,220,185,210,205,25,33]
# print(list(filter(lambda num: num % 15 == 0, nums)))
# first = [1,1,2,3,5,8,13,21,34,55,89]
# second = [2,3,5,8,13,21,34,55,89]
# def add(first,second):
#     a = []
#     for i in first:
#         for j in second:
#             if i == j:
#                 a.append(i)
#                 break
#     return a
# print(add(first,second))
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return (self.width + self.height) * 2
#     def __str__(self):
#         area = self.area()
#         perimeter = self.perimeter()
#         return f"Output:{self.width,self.height,area,perimeter}"
# rectangle = Rectangle(10,20)
# print(rectangle)
# class Book:
#     def __init__(self,name,author=None,date=None) -> None:
#         self.name = name
#         self.author = author if author else ''
#         self.date = date if date else ''
#     def display(self):
#         print( f"{self.name:<30} {self.author:20} {self.date:>5}")
#
# class Library:
#     def __init__(self,name,books=None):
#         self.name = name
#         self.books = books if books else []
#     def list_books(self):
#         for book in self.books:
#             book.display()
#     def filter(self,name='',author='',date=None):
#         filter_list = []
#         for book in self.books:
#             if (not name or name.capitalize() in book.name.capitalize()) and \
#                     (not author or author.capitalize() in book.author.capitalize()) and \
#                     (date is None or date == book.date):
#                 filter_list.append(book)
#         return filter_list
#     def delete_book(self,book):
#         if book in self.books:
#             self.books.remove(book)
#         else:
#             print("Такой книги нет")
#     def add_book(self,book):
#         self.books.append(book)
#     @staticmethod
#     def as_table(book_list):
#         for book in book_list:
#             book.display()
# book = Book('Title', 'Author')
# book_1 = Book('Чистый код', 'Дядя Боб', 2017)
# book_2 = Book('От 2 до 5', 'Корней Чуковский', 1958)
# book_3 = Book('Идеальный программист', 'Дядя Боб', 2018)
# book_4 = Book('Рецепты татарской кухни', date=2018)
# library = Library('Домашняя библиотека')
# library.add_book(book)
# library.add_book(book_1)
# library.add_book(book_2)
# library.add_book(book_3)
# library.add_book(book_4)
# print(library.name)
# library.list_books()
# library.delete_book(book_4)
# # library.list_books()
# class Good:
#     def __init__(self, name, price,count = 1):
#         self.name = name
#         self.price = price
#         self.count = count
#     def total_price(self):
#         return self.price * self.count
#     def __str__(self):
#         return (f"{self.name:<20} {self.price:>7.2f} * {self.count:>3} = {self.total_price():>7.2f}")
# class DiscountGood(Good):
#     def __init__(self, name, price, count=1,discount=25):
#         super().__init__(name, price,count)
#         self.discount = discount
#     def total_price(self):
#         return super().total_price() * (1- self.discount / 100)
#     def __str__(self):
#         return super().__str__()  + f"(-{self.discount}%)"
# class Cart:
#     def __init__(self, goods):
#         self.goods = goods
#     def total_price_all(self):
#         total = 0
#         for goods in self.goods:
#             total += goods.total_price()
#         return total
#     def __str__(self) -> str:
#         result = ""
#         print(f"{'Name':<20} {'PPU':>7} {'CNT':>5} {'Price':>7} {'Disc.':>7}")
#         for good in self.goods:
#             result += str(good) + "\n"
#         result += f"\nTotal: {self.total_price_all():.2f}"
#         return result
# goods = [
#     Good('Bread', 17, 3),
#     Good('Water', 19, 2),
#     DiscountGood('Juice', 80,  1,20),
#     Good('Toilet Paper', 19, 10)
# ]
# cart = Cart(goods)
# print(cart)
# class Field:
#     def __init__(self):
#         self.fields = [[" " for _ in range(3)]for _ in range(3)]
#     def filling(self,row,cell,symbol):
#         try:
#             if not (0 <= row < 3 and 0 <= cell < 3):
#                 raise ValueError("Число больше")
#             if self.fields[row][cell] != ' ':
#                 raise ValueError("Поле занято")
#             self.fields[row][cell] = symbol
#         except ValueError as e:
#             print("Ошибка",e)
#             return False
#         return True
#     def display(self):
#         for row in self.fields:
#             print(" | ".join(row))
#             print("-" * (3 * 4 - 3))
# class Player:
#     def __init__(self,symbol,field):
#         self.symbol = symbol
#         self.field = field
#     def make_move(self):
#         while True:
#             try:
#                 row = int(input(f"Введите строку {self.symbol} (1-3): ")) - 1
#                 cell = int(input(f"Введите столбец {self.symbol} (1-3): ")) - 1
#                 if self.field.filling(row,cell,self.symbol):
#                     break
#             except ValueError:
#                 print("Ошибка")
# import random
# class Bot(Player):
#     def make_move(self):
#         while True:
#             row = random.randint(0,2)
#             cell = random.randint(0,2)
#             if self.field.filling(row,cell,self.symbol):
#                 print(f"Бот {self.symbol} поставил в ({row + 1},{cell + 1})")
#                 break
# class Checker:
#     def __init__(self,field):
#         self.field = field
#     def check_win(self,player):
#         s = player.symbol
#         f = self.field.fields
#         for row in f:
#             if all(cell == s for cell in row):
#                 return True
#         for col in range(3):
#             if all(f[row][col] == s for row in range(3)):
#                 return True
#         if f[0][0] == s and f[1][1] == s and f[2][2] == s:
#             return True
#         if f[0][2] == s and f[1][1] == s and f[2][0] == s:
#             return True
#         return False
#
#     def draw(self):
#         for row in self.field.fields:
#             for cell in row:
#                 if cell == " ":
#                     return False
#         return True
# class Game:
#     def __init__(self):
#         self.field = Field()
#         self.checker = Checker(self.field)
#     def main(self):
#         user_input = input("Выберите режим: ")
#         if user_input == "1":
#             self.player1 = Player('x', self.field)
#             self.player2 = Bot('o', self.field)
#         elif user_input == "2":
#             self.player1 = Player('x', self.field)
#             self.player2 = Player('o', self.field)
#         if user_input == "1" or user_input == "2":
#             while True:
#                 self.player1.make_move()
#                 self.field.display()
#                 if self.checker.check_win(self.player1):
#                     print("Игрок 1 победил")
#                     break
#                 if self.checker.draw():
#                     print("Ничья!")
#                     break
#                 self.player2.make_move()
#                 self.field.display()
#                 if self.checker.check_win(self.player2):
#                     print("Игрок 2 победил!")
#                     break
#                 if self.checker.draw():
#                     print("Ничья!")
#                     break
#         elif user_input == "exit":
#             exit()
#         else:
#             print("\nНекорректный режим игры. Выберите 1 или 2\n")
#             self.main()

# field = Field()
# player1 = Player('x', field)
# player2 = Bot('o', field)
#
# for _ in range(3):
#     print("\n--->Игрок 1 (Его фигура: X)\n")
#     player1.make_move()
#     field.display()
#
#     print("\n--->Бот (Его фигура: O)")
#     player2.make_move()
#     field.display()

class Animal:
    def __init__(self,name,age,hp,mood,satiety):
        self.name = name
        self.age = age
        self.hp = hp
        self.mood = mood
        self.satiety = satiety
        self.average_level = (self.hp + self.mood + self.satiety) // 3

    def display(self, index):
        print(
            f"{index:<3}{self.name:<10}{self.age:<10}{self.hp:<12}"
            f"{self.mood:<14}{self.satiety:<10}{self.average_level:<10}"
        )
import random
class Game:
    def __init__(self):
        self.animals = [
            Animal("Peach", 11, 78, 86, 50),
            Animal("Jasper", 12, 39, 43, 39),
            Animal("Poppy", 9, 38, 57, 71),
        ]
    def add_animal(self):
        while True:
            name = input("Введите имя: ")
            if name:
                break
            print("Имя не может быть пустым. Попробуйте ещё раз.")
        while True:
            age_input = input("Введите возраст: ")
            if not age_input.isdigit():
                print("Введите только число, без символов/букв.")
                continue
            age = int(age_input)
            if not 1 <= age <= 18:
                print("❗ Возраст должен быть от 1 до 18.")
            else:
                break
        hp = random.randint(20, 100)
        mood = random.randint(20, 100)
        satiety = random.randint(20, 100)
        new_animal = Animal(name, age, hp, mood, satiety)
        self.animals.append(new_animal)
    def action_animals(self):
        actions = ["Кормить кота","Играть с котом","Лечить кота"]
        action = input("Выберите действие: ")

    def show_animals(self):
        for i, pet in enumerate(self.animals, start=1):
            pet.display(i)
game = Game()
    self.animals.sort(key=lambda x: x.average_level, reverse=True)
        print(f"{'#':<3}{'имя':<10}{'возраст':<10}{'здоровье':<12}"
              f"{'настроение':<14}{'сытость':<10}{'средний':<10}")
       
game.show_animals()
game.add_animal()
game.show_animals()