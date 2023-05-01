# Задание 1
# Создайте класс Circle (окружность). Для данного
# класса реализуйте ряд перегруженных операторов:
# ■ Проверка на равенство радиусов двух окружностей
# (операция = =);
# ■ Сравнения длин двух окружностей (операции >, <,
# <=,>=);
# ■ Пропорциональное изменение размеров окружности,
# путем изменения ее радиуса (операции + - += -=).

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def length_circle(self):
#         return 2 * 3.14 * self.radius
#
#     def area_circle(self):
#         return 3.14 * self.radius ** 2
#
#     def __str__(self):
#         return (f'У окружности с радиусом {self.radius} длина окружности - {self.length_circle()}, '
#                 f'площадь круга {self.area_circle()}')
#
#     def __eq__(self, other):
#         if self.radius == other.radius:
#             return 'Радиусы равны!'
#         return 'Радиусы не равны'
#
# # Если радиус больше, то и длина окружности больше.
# # Поэтому при сравнении использовала радиус, а не переменную с длиной окружности или формулу
#     def __lt__(self, other):
#         return self.radius < other.radius
#
#     def __le__(self, other):
#         return self.radius <= other.radius
#
#     def __gt__(self, other):
#         return self.radius > other.radius
#
#     def __ge__(self, other):
#         return self.radius >= other.radius
#
#     def __add__(self, other):
#         return self.radius + other.radius
#
#     def __iadd__(self, radius):
#         self.radius += radius
#         return self
#
#     def __sub__(self, other):
#         return self.radius - other.radius
#
#     def __isub__(self, radius):
#         self.radius -= radius
#         return self
#
#
# a = Circle(5)
# print(a)
# b = Circle(6)
# print(b)
# c = Circle(5.001)
# print(c)
# d = Circle(5)
# print(d)
# print(a == b)
# print(a == d)
# print(a + b)
# print(c - a)
# print(a <= c)
# print(a > b)


# Задание 2
# Создайте класс Complex (комплексное число). Более
# подробно ознакомиться с комплексными числами можно
# по ссылке.
# Создайте перегруженные операторы для реализации
# арифметических операций для по работе с комплексными
# числами (операции +, -, *, /).

# class Complex:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return f'Привет, я - комплексное число ({self.a}) + ({self.b})i'
#
#     def __add__(self, other):
#         if self.b + other.b >= 0:
#             return f'{self.a + other.a} + {self.b + other.b}i'
#         else:
#             return f'{self.a + other.a} - {(self.b + other.b) * -1}i'
#
#     def __sub__(self, other):
#         if self.b - other.b >= 0:
#             return f'{self.a - other.a} + {self.b - other.b}i'
#         else:
#             return f'{self.a - other.a} - {(self.b - other.b) * -1}i'
#
#     def __mul__(self, other):
#         if self.a * other.a + self.b * other.b >= 0:
#             return f'{(self.a * other.a - self.b * other.b)} + {(self.a * other.a + self.b * other.b)}i'
#         else:
#             return f'{(self.a * other.a - self.b * other.b)} - {(self.a * other.a + self.b * other.b) * -1}i'
#
#     def __truediv__(self, other):
#         if other.a ** 2 + other.b ** 2 != 0:
#             if (self.b * other.b - self.a * other.a) // (other.a + other.b) >= 0:
#                 return f'{(self.a * other.a + self.b * other.b) // (other.a + other.b)} + ' \
#                    f'{(self.b * other.b - self.a * other.a) // (other.a + other.b)}i'
#             else:
#                 return f'{(self.a * other.a + self.b * other.b) // (other.a + other.b)} - ' \
#                    f'{((self.b * other.b - self.a * other.a) // (other.a + other.b)) * -1}i'
#
#         else:
#             return 'Делить на 0 нельзя'
#
#
# object1 = Complex(10, -6)
# object2 = Complex(5, 3)
# print(object1)
# print(object2)
# print(object1 + object2)
# print(object1 - object2)
# print(object1 * object2)
# print(object1 / object2)
# object3 = Complex(10, 6)
# print(object3)
# print(object3 + object2)
# print(object3 - object2)
# print(object3 * object2)
# print(object3 / object2)


# Задание 3
# Вам необходимо создать класс Airplane (самолет).
# С помощью перегрузки операторов реализовать:
# ■ Проверка на равенство типов самолетов (операция
# = =);
# ■ Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
# ■ Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции >
# < <= >=).

# class Airplane:
#     def __init__(self, type_airplane, num_passengers, max_passengers):
#         self.type_airplane = type_airplane
#         self.num_passengers = num_passengers
#         self.max_passengers = max_passengers
#     def __str__(self):
#         return f'В самолете типа {self.type_airplane} сейчас находятся {self.num_passengers} пассажиров. ' \
#                f'Максимально возможное количество пассажиров на борту - {self.max_passengers}.'
#
#
#     def __eq__(self, other):
#         if self.type_airplane == other.type_airplane:
#             return 'Типы самолетов равны'
#         else:
#             return 'Это разные типы самолетов'
#
#     def __add__(self, other):
#         if self.num_passengers + other < self.max_passengers:
#             return f'Число пассажиров на борту увеличилось на {other} и составляет {self.num_passengers + other} человек'
#         return 'Число пассажиров превышает максимально возможное'
#
#     def __sub__(self, other):
#         if self.num_passengers - other > 0:
#             return f'Число пассажиров на борту уменьшилось на {other} и составляет {self.num_passengers - other} человек'
#         return 'Число пассажиров не может быть меньше 0'
#
#     def __iadd__(self, other):
#         return f'Число пассажиров на борту составляет {self.num_passengers + self.num_passengers} человек'
#
#     def __isub__(self, other):
#         return f'Число пассажиров на борту составляет {self.num_passengers - self.num_passengers} человек'
#
#     def __gt__(self, other):
#         return self.max_passengers > other.max_passengers
#
#     def __ge__(self, other):
#         return self.max_passengers >= other.max_passengers
#
#     def __lt__(self, other):
#         return self.max_passengers < other.max_passengers
#
#     def __le__(self, other):
#         return self.max_passengers <= other.max_passengers
#
#
# a = Airplane('Sukhoi Superjet 100', 20, 98)
# b = Airplane('MC-21', 75, 180)
# c = Airplane('ИЛ-96', 210, 280)
# d = Airplane('Sukhoi SuperJet 100', 81, 98)
# print(a)
# print(b)
# print(c)
# print(d)
# print(a + 50)
# print(b - 10)
# print(a < b)
# print(a > c)
# print(a == d)


# Задание 4
# Создать класс Flat (квартира). Реализовать перегруженные операторы:
# ■ Проверка на равенство площадей квартир (операция
# ==);
# ■ Проверка на неравенство площадей квартир (операция !=);
# ■ Сравнение двух квартир по цене (операции > < <= >=).
#
# class Flat:
#     def __init__(self, area, price):
#         self.area = area
#         self.price = price
#
#     def __str__(self):
#         return f'Эта квартира площадью {self.area} квадратных метров стоит {self.price} рублей.'
#
#     def __eq__(self, other):
#         return self.area == other.area
#
#     def __ne__(self, other):
#         return self.area != other.area
#
#     def __gt__(self, other):
#         return self.price > other.price
#
#     def __ge__(self, other):
#         return self.price >= other.price
#
#     def __lt__(self, other):
#         return self.price < other.price
#
#     def __le__(self, other):
#         return self.price <= other.price
#
#
# a = Flat('100 м2', '1000')
# b = Flat('80 м2', '1200')
# c = Flat('120 м2', '3000')
# d = Flat('100 м2', '1500')
# print(a)
# print(b)
# print(c)
# print(d)
# print(a == c)
# print(a != b)
# print(a == d)
# print(a > b)
# print(c >= d)

