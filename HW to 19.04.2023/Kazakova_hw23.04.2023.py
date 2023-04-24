# Задание 1
# Создайте класс Device, который содержит информацию об устройстве.
# С помощью механизма наследования, реализуйте класс
# CoffeeMachine (содержит информацию о кофемашине)
# класс Blender (содержит информацию о блендере), класс
# MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые
# для работы методы.

# class Device:
#     def __init__(self, manufacture, model, power, country, control_type, housing_material, child_protection, price):
#         self.manufacture = manufacture
#         self.model = model
#         self.power = power
#         self.country = country
#         self.control_type = control_type
#         self.housing_material = housing_material
#         self.child_protection = child_protection
#         self.price = price
#
#     def add(self):
#         self.manufacture = input('Введите производителя: ')
#         self.model = input('Введите модель: ')
#         self.power = input('Введите мощность: ')
#         self.country = input('Введите страну производителя: ')
#         self.control_type = input('Введите тип управления: ')
#         self.housing_material = input('Введите материал корпуса: ')
#         self.child_protection = input('Есть ли защита от детей(да/нет): ')
#         self.price = input('Введите цену: ')
#
#     def print(self):
#         print(f' {self.manufacture}, {self.model}: \n'
#               f'Мощность {self.power}, страна производитель {self.country}, '
#               f'тип управления {self.control_type},'
#               f' материал корпуса {self.housing_material}, '
#               f'защита от детей {self.child_protection}, цена {self.price}')
#
#
# class CoffeeMachine(Device):
#     count = 0
#     def __init__(self, manufacture, model, power, country, control_type,
#                  housing_material, child_protection, price, type_of_coffee):
#         super().__init__(manufacture, model, power, country, control_type, housing_material, child_protection, price)
#         self.type_of_coffee = type_of_coffee
#
#     def print(self):
#         print(f'{self.manufacture}, {self.model}: \n'
#               f'Мощность {self.power}, страна производитель {self.country}, '
#               f'тип управления {self.control_type},'
#               f' материал корпуса {self.housing_material}, '
#               f'защита от детей {self.child_protection}, цена {self.price} руб.')
#
#
#     def operation(self):
#         self.type_of_coffee = input('1 - американо\n'
#                                     '2- капучино\n'
#                                     '3 - латте\n'
#                                     '4 - горячий шоколад\n'
#                                     'Выберите тип кофе: ')
#         print('Идёт приготовление напитка ...')
#         print('.')
#         print('....ζ ')
#         print('ᴄ(¯¯)"...ζ')
#         print('¯¯¯¯¯ᴄ(¯¯)"')
#         print('¯¯¯¯¯¯¯¯¯¯¯')
#         print()
#
#
# class Blender(Device):
#     def __init__(self, manufacture, model, power, country, control_type,
#                  housing_material, child_protection, price, speed):
#         super().__init__(manufacture, model, power, country, control_type,
#                          housing_material, child_protection, price)
#         self.speed = speed
#
#     def operation(self):
#         self.speed = input('Выберите скорость(1-8): \n')
#         print('Жжжж - жжж - жжж...')
#
#
# class MeatGrinder(Device):
#     def __init__(self, manufacture, model, power, country, control_type,
#                  housing_material, child_protection, price, start_revers):
#         super().__init__(manufacture, model, power, country, control_type,
#                          housing_material, child_protection, price)
#         self.start_revers = start_revers
#
#     def operation(self):
#         self.start_revers = input('Выберите режим(1-старт / 2-реверс): ')
#         if self.start_revers == 1:
#             print('Вжжж - жжж - жжж...')
#         elif self.start_revers == 2:
#             print('дрр - брр - брррр...')
#         else:
#             print('Проверьте, включен ли Ваш прибор в сеть')
#
#
# a = CoffeeMachine('Saeco', 'Aulika', 1400, 'A++', 'electronic', 'metal, plastic', 'yes', '140000', 3)
# a.operation()
# a.print()
#
# b = Blender('Bosh', '123QWE', 1200, 'A', 'mechanic', 'plastic, metal', 'no', '4000', 7)
# b.operation()
#
# c = MeatGrinder('Phillips', '098uhb', 1200, 'A+', 'electronic', 'metal', 'no', '12000', 1)
# c.operation()


# Задание 2
# Создайте класс Ship, который содержит информацию
# о корабле.
# С помощью механизма наследования, реализуйте
# класс Frigate (содержит информацию о фрегате), класс
# Destroyer (содержит информацию об эсминце), класс
# Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые
# для работы методы.
#
# class Ship:
#     def __init__(self, name, year, displacement, length, speed, cruising_range, crew):
#         self.name = name
#         self.year = year
#         self.displacement = displacement
#         self.length = length
#         self.speed = speed
#         self.cruising_range = cruising_range
#         self.crew = crew
#
#     def add(self):
#         self.name = input('name')
#         self.year = input('year')
#         self.displacement = input('displacement')
#         self.length = input('length')
#         self.speed = input('speed')
#         self.cruising_range = input('cruising_range')
#         self.crew = input('crew')
#
#     def __str__(self):
#         return self.name
#
#
# class Frigate(Ship):
#     def __init__(self, name, year, displacement, length, speed, cruising_range, crew):
#         super().__init__(name, year, displacement, length, speed, cruising_range, crew)
#         self.target = 'поиска и уничтожения атомных подводных лодок в море, противолодочного охранения, \n' \
#                       ' противовоздушной и противоракетной обороны авианосцев'
#     def print_target(self):
#         print(f'Я - {Frigate.__name__} {self.name} и я нужен для {self.target}')
#         print()
#
#
# class Destroyer(Ship):
#     def __init__(self, name, year, displacement, length, speed, cruising_range, crew):
#         super().__init__(name, year, displacement, length, speed, cruising_range, crew)
#         self.target = 'борьбы с подводными лодками, летательными аппаратами (в том числе ракетами)\n' \
#                       ' и кораблями противника, а также для охраны и обороны соединений кораблей \n' \
#                       'или конвоев судов при переходе морем, иногда для разведывательной и дозорной \n' \
#                       'службы, артиллерийской поддержки при высадке десанта и для постановки минных \n' \
#                       'заграждений, а также дымовых завес'
#
#     def print_target(self):
#         print(f'Я - {Destroyer.__name__} {self.name} и я нужен для {self.target}')
#         print()
#
# class Cruiser(Ship):
#     def __init__(self, name, year, displacement, length, speed, cruising_range, crew):
#         super().__init__(name, year, displacement, length, speed, cruising_range, crew)
#         self.target = 'того, чтобы независимо от основного флота бороться с лёгкими силами флота противника, \n' \
#                       'оборонять соединения боевых кораблей и конвоев судов, оказывать огневую поддержку приморских\n' \
#                       'флангов сухопутных войск и обеспечивать высадку морских десантов, постановку минных заграждений.'
#
#     def print_target(self):
#         print(f'Я - {Cruiser.__name__} {self.name} и я нужен для {self.target}')
#         print()
#
# a = Frigate('Адмирал Горшков', '2018', '4500 тонн', '135 метров', '29 узлов', '4000 миль', '180-210 человек')
# a.print_target()
#
# b = Destroyer('Адмирал Ушаков', '1993', '6600 тонн', '156 метра', '32 узла', '3920 миль', '350 человек')
# b.print_target()
#
# c = Cruiser('Пётр Великий', '1998', '24300 тонн', '252 метра', '32 узла', '1000 миль', '760 человек')
# c.print_target()


# Задание 3
# Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами.
# В классе должны быть предусмотрены поле для хранения целой части денег (доллары, евро, рубли и т.д.) и
# поле для хранения копеек (центы, евро-центы, копейки и т.д.).
# Реализовать методы для вывода суммы на экран, задания значений для частей.

from abc import ABC, abstractmethod

class Money:
    def __init__(self, currency, integer_part, fractional_part):
        self.currency = currency
        self.integer_part = integer_part
        self.fractional_part = fractional_part

    def print(self):
        print(f'Сумма {self.integer_part}.{self.fractional_part} {self.currency}')
    @abstractmethod
    def currency(self):
        pass

    @abstractmethod
    def integer_part(self):
        pass

    @abstractmethod
    def fractional_part(self):
        pass


class Rubles(Money):
    @property
    def get_summ(self):
        return f'Сумма {self.integer_part}.{self.fractional_part} {self.currency}'

class Dollars(Money):
    @property
    def get_summ(self):
        return f'Сумма {self.integer_part}.{self.fractional_part} {self.currency}'

class Euros(Money):
    @property
    def get_summ(self):
        return f'Сумма {self.integer_part}.{self.fractional_part} {self.currency}'

a = Rubles('rub', 2, 45)
a.get_summ

