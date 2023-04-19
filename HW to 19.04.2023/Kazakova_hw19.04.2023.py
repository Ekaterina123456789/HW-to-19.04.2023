# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
#
# class Cars:
#     def __init__(self, manufacture, model, year, v_motor, color, price):
#         self.manufacture = manufacture
#         self.model = model
#         self.year = year
#         self.v_motor = v_motor
#         self.color = color
#         self.price = price

#     def add(self):
#         self.manufacture = input('Введите производителя: ')
#         self.model = input('Введите название модели: ')
#         self.year = input('Введите год выпуска тс: ')
#         self.v_motor = input('Введите объём двигателя: ')
#         self.color = input('Введите цвет автомобиля: ')
#         self.price = input('Введите цену: ')

#     def print(self):
#         print(f'Производитель: {self.manufacture}')
#         print(f'Модель: {self.model}')
#         print(f'Год выпуска: {self.year}')
#         print(f'Объём двигателя: {self.v_motor}')
#         print(f'Цвет: {self.color}')
#         print(f'Цена: {self.price}')

#     def reset_price(self):
#         self.price = input('Введите новую цену автомобиля: ')
#         return 'Цена изменена и составляет {self.color}'

#     def add_color(self):
#         new_color = (input('Введите цвет для добавления: '))
#         self.color = (self.color, new_color)
#         print(f'Новый цвет добавлен: {self.color}')
#
#
# VolvoXC90 = Cars('Вольво', 'XC90', '2018', '2.0', 'черный', '3500000')
# VolvoXC90.print()
# VolvoXC90.add_color()
# VolvoXC90.print()
# VolvoXC90.reset_price()
# VolvoXC90.print()


# Задание 2.
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.


# class Book:
#     def __init__(self, name, year, publisher, genre, autor, price):
#         self.name = name
#         self.year = year
#         self.publisher = publisher
#         self.genre = genre
#         self.autor = autor
#         self.price = price
#
#     def __add__(self, other):
#         self.name = input('Введите название книги: ')
#         self.year = input('Введите год выпуска: ')
#         self.publisher = input('Введите издательство: ')
#         self.genre = input('Введите жанр: ')
#         self.autor = input('Введите автора: ')
#         self.price = input('Введите цену: ')
#     def print(self):
#         print(f'{self.name}, {self.year}г., издательство {self.publisher}, жанр {self.genre}, автор {self.autor}, цена {self.price}')
#
#     def reset_price(self):
#         self.price = input('Введите новую цену: ')
#         return 'Цена изменена и составляет {self.color}'
#
#     def reset_genre(self):
#         self.genre = input('Введите новый жанр: ')
#         return 'Новый жанр добавлен!'
#
#
# a = Book("Приключения Тома Сойера", '2018', "Самовар", "Художественная литература", "Марк Твен", "385 руб.")
# a.print()
# a.reset_price()
# a.reset_genre()
# a.print()


# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

class Stadium:
    def __init__(self, name, data, country, city, capacity):
        self.name = name
        self.data = data
        self.country = country
        self.city = city
        self.capacity = capacity

    def __add__(self, other):
        self.name = input('Введите название стадиона: ')
        self.data = input('Введите дату открытия: ')
        self.country = input('Введите страну: ')
        self.city = input('Введите город: ')
        self.capacity = input('Введите вместимость: ')

    def print(self):
        print(f'Название стадиона: {self.name}\n'
              f'Дата открытия: {self.data}\n'
              f'Страна: {self.country}\n'
              f'Город: {self.city}\n'
              f'Вместимость: {self.capacity} человек')
        print("*" * 20)

    def reset_capacity(self):
        self.capacity = input('Измените вместимость: ')
        return f'Вместимость стадиона {self.name} изменена на {self.capacity}'

    def reset_city(self):
        self.city = input('Введите новый город: ')
        return f'Новый город {self.city}'


a = Stadium('Лужники', '1956', 'Москва', 'Россия', '81000')
b = Stadium('Казань Арена', '2013', 'Казань', 'Россия', '45379')
a.print()
b.print()
a.reset_city()
b.reset_capacity()
a.print()
b.print()



