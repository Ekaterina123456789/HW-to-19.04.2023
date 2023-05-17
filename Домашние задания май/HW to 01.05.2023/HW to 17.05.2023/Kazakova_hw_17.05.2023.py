# Задание 1
# К уже реализованному классу «Автомобиль» добавьте
# возможность упаковки и распаковки данных с использованием json и pickle.

# import pickle
# import json
#
#
# class Cars:
#     def __init__(self, manufacture, model, year, v_motor, color, price):
#         self.manufacture = manufacture
#         self.model = model
#         self.year = year
#         self.v_motor = v_motor
#         self.color = color
#         self.price = price
#
#     def add(self):
#         self.manufacture = input('Введите производителя: ')
#         self.model = input('Введите название модели: ')
#         self.year = input('Введите год выпуска тс: ')
#         self.v_motor = input('Введите объём двигателя: ')
#         self.color = input('Введите цвет автомобиля: ')
#         self.price = input('Введите цену: ')
#
#     def print(self):
#         print(f'Производитель: {self.manufacture}')
#         print(f'Модель: {self.model}')
#         print(f'Год выпуска: {self.year}')
#         print(f'Объём двигателя: {self.v_motor}')
#         print(f'Цвет: {self.color}')
#         print(f'Цена: {self.price}')
#
#     def reset_price(self):
#         self.price = input('Введите новую цену автомобиля: ')
#         return 'Цена изменена и составляет {self.color}'
#
#     def add_color(self):
#         new_color = (input('Введите цвет для добавления: '))
#         self.color = (self.color, new_color)
#         print(f'Новый цвет добавлен: {self.color}')
#
#     def save_pickle(self, filename):
#         with open(filename, 'wb') as f:
#             pickle.dump(self, f)
#
#     @staticmethod
#     def load_pickle(filename):
#         try:
#             with open(filename, 'rb') as f:
#                 return pickle.load(f)
#         except FileNotFoundError:
#             print('Incorrect filepath provided!')
#
#     def save_json(self, filename):
#         with open(filename, 'w') as f:
#             json.dump(self.__dict__, f)
#
#     @staticmethod
#     def load_json(filename):
#         with open(filename, 'r') as f:
#             cars_dict = json.load(f)
#             return Cars(**cars_dict)
#
#
# VolvoXC90 = Cars('Вольво', 'XC90', '2018', '2.0', 'черный', '3500000')
# VolvoXC90.print()
# VolvoXC90.add_color()
# VolvoXC90.print()
# VolvoXC90.reset_price()
# VolvoXC90.print()
# VolvoXC90.save_json("cars.json")
# new_VolvoXC90 = Cars.load_json('cars.json')
# print(new_VolvoXC90)
# VolvoXC90.save_pickle('cars.txt')
# new_cars = Cars.load_pickle('cars.txt')
# print(new_cars)


# Задание 2
# К уже реализованному классу «Книга» добавьте возможность упаковки и распаковки данных с использованием json и pickle.

import pickle
import json


class Book:
    def __init__(self, name, year, publisher, genre, autor, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.autor = autor
        self.price = price

    def __add__(self, other):
        self.name = input('Введите название книги: ')
        self.year = input('Введите год выпуска: ')
        self.publisher = input('Введите издательство: ')
        self.genre = input('Введите жанр: ')
        self.autor = input('Введите автора: ')
        self.price = input('Введите цену: ')
    def print(self):
        print(f'{self.name}, {self.year}г., издательство {self.publisher}, жанр {self.genre}, автор {self.autor}, цена {self.price}')

    def reset_price(self):
        self.price = input('Введите новую цену: ')
        return 'Цена изменена и составляет {self.color}'

    def reset_genre(self):
        self.genre = input('Введите новый жанр: ')
        return 'Новый жанр добавлен!'

    def save_pickle(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load_pickle(filename):
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            print('Incorrect filepath provided!')

    def save_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.__dict__, f)

    @staticmethod
    def load_json(filename):
        with open(filename, 'r') as f:
            books_dict = json.load(f)
            return Book(**books_dict)


a = Book("Приключения Тома Сойера", '2018', "Самовар", "Художественная литература", "Марк Твен", "385 руб.")
a.print()
a.reset_price()
a.reset_genre()
a.print()
a.save_json('books.json')
new_a = Book.load_json('books.json')
print(new_a)
a.save_pickle('books.txt')
new_a = Book.load_pickle('books.txt')
print(new_a)


# Задание 3
# К уже реализованному классу «Стадион» добавьте
# возможность упаковки и распаковки данных с использованием json и pickle

# import pickle
# import json
#
#
# class Stadium:
#     def __init__(self, name, data, country, city, capacity):
#         self.name = name
#         self.data = data
#         self.country = country
#         self.city = city
#         self.capacity = capacity
#
#     def __add__(self, other):
#         self.name = input('Введите название стадиона: ')
#         self.data = input('Введите дату открытия: ')
#         self.country = input('Введите страну: ')
#         self.city = input('Введите город: ')
#         self.capacity = input('Введите вместимость: ')
#
#     def reset_capacity(self):
#         self.capacity = input('Измените вместимость: ')
#         return f'Вместимость стадиона {self.name} изменена на {self.capacity}'
#
#     def reset_city(self):
#         self.city = input('Введите новый город: ')
#         return f'Новый город {self.city}'
#
#     def save_pickle(self, filename):
#         with open(filename, 'wb') as f:
#             pickle.dump(self, f)
#
#     @staticmethod
#     def load_pickle(filename):
#         try:
#             with open(filename, 'rb') as f:
#                 return pickle.load(f)
#         except FileNotFoundError:
#             print('Incorrect filepath provided!')
#
#     def save_json(self, filename):
#         with open(filename, 'w') as f:
#             json.dump(self.__dict__, f)
#
#     @staticmethod
#     def load_json(filename):
#         with open(filename, 'r') as f:
#             stadium_dict = json.load(f)
#             return Stadium(**stadium_dict)
#
#     def __str__(self):
#         return f'Название стадиона: {self.name}\n Дата открытия: {self.data}\n Страна: {self.country}\n Город: {self.city}\n Вместимость: {self.capacity} человек\n' \
#               f'********************'
#
#
# a = Stadium('Лужники', '1956', 'Москва', 'Россия', '81000')
# b = Stadium('Казань Арена', '2013', 'Казань', 'Россия', '45379')
# a.save_pickle('stadium.txt')
# new_stadium = Stadium.load_pickle('stadium.txt')
# print(new_stadium)
# new_stadium.reset_capacity()
# new_stadium.reset_city()
# print(new_stadium)
# b.save_json('stadium.json')
# new_b = Stadium.load_json('stadium.json')
# print(new_b)
