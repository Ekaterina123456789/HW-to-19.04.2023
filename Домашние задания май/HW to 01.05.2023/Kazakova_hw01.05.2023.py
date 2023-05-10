############# Задание 1
# Создайте базовый класс Фигура с методом для подсчета
# площади. Создать производные классы: прямоугольник,
# круг, прямоугольный треугольник, трапеция со своими
# методами для подсчета площади.

# class Figure:
#     def __init__(self):
#         self.a = 0
#
#     @property
#     def area(self):
#         return None
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height):
#         Figure.__init__(self)
#         self.width = width
#         self.height = height
#
#     @property
#     def area(self):
#         return self.height * self.width
#
#
# class Circle(Figure):
#     def __init__(self, radius):
#         Figure.__init__(self)
#         self.radius = radius
#
#     @property
#     def area(self):
#         return 3.14 * self.radius ** 2
#
#
# class RightTriangle(Figure):
#     def __init__(self, base, height):
#         Figure.__init__(self)
#         self.base = base
#         self.height = height
#
#     @property
#     def area(self):
#         return 0.5 * self.base * self.height
#
#
# class Trapezium(Figure):
#     def __init__(self, base1, base2, height):
#         Figure.__init__(self)
#         self.base1 = base1
#         self.base2 = base2
#         self.height = height
#
#     @property
#     def area(self):
#         return 0.5 * (self.base1 + self.base2) * self.height
#
#
# a = Rectangle(10, 5)
# print(a.area)
# b = Circle(10)
# print(b.area)
# c = RightTriangle(10, 8)
# print(c.area)
# d = Trapezium(10, 5, 8)
# print(d.area)

############# Задание 2
# Для классов из задания 1 нужно переопределить магические методы int(возвращает площадь) и str(возвращает
# информацию о фигуре).
#
# class Figure:
#     def __init__(self):
#         self.a = 0
#
#     @property
#     def area(self):
#         return None
#
#     def __str__(self):
#         return f'Это геометрическая фигура'
#
#     def __int__(self):
#         return int(self.a)
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height):
#         Figure.__init__(self)
#         self.width = width
#         self.height = height
#
#     @property
#     def area(self):
#         return self.height * self.width
#
#     def __str__(self):
#         return f'Это геометрическая фигура - прямоугольник'
#
#     def __int__(self):
#         return int(self.area)
#
#
# class Circle(Figure):
#     def __init__(self, radius):
#         Figure.__init__(self)
#         self.radius = radius
#
#     @property
#     def area(self):
#         return 3.14 * self.radius ** 2
#
#     def __str__(self):
#         return f'Это геометрическая фигура - круг'
#
#     def __int__(self):
#         return int(self.area)
#
#
# class RightTriangle(Figure):
#     def __init__(self, base, height):
#         Figure.__init__(self)
#         self.base = base
#         self.height = height
#
#     @property
#     def area(self):
#         return 0.5 * self.base * self.height
#
#     def __str__(self):
#         return f'Это геометрическая фигура - прямоугольный треугольник'
#
#     def __int__(self):
#         return int(self.area)
#
#
# class Trapezium(Figure):
#     def __init__(self, base1, base2, height):
#         Figure.__init__(self)
#         self.base1 = base1
#         self.base2 = base2
#         self.height = height
#
#     @property
#     def area(self):
#         return 0.5 * (self.base1 + self.base2) * self.height
#
#     def __str__(self):
#         return f'Это геометрическая фигура - трапеция'
#
#     def __int__(self):
#         return int(self.area)
#
#
# a = Rectangle(10, 5)
# print(a)
# b = Circle(10)
# print(b)
# c = RightTriangle(10, 8)
# print(c)
# d = Trapezium(10, 5, 8)
# print(d)


############# Задание 3
# Создайте базовый класс Shape для рисования плоских
# фигур.
# Определите методы:
# ■ Show() — вывод на экран информации о фигуре;
# ■ Save() — сохранение фигуры в файл;
# ■ Load() — считывание фигуры из файла.
# Определите производные классы:
# ■ Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
# ■ Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами;
# ■ Circle — окружность с заданными координатами центра и радиусом;
# ■ Ellipse — эллипс с заданными координатами верхнего
# угла описанного вокруг него прямоугольника со сторонами, параллельными осям координат, и размерами
# этого прямоугольника.
# Создайте список фигур, сохраните фигуры в файл,
# загрузите в другой список и отобразите информацию о каждой из фигур


class Shape:
    shapes = []
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @staticmethod
    def add(self):
        shapes.append(self.x)
        shapes.append(self.y)

    @classmethod
    def show(self):
        print(f'Это {cls.__name__}')

    @staticmethod
    def save(self, file):
        with open(file, 'w') as file_out:
            file_out.writelines(shapes)

    @staticmethod
    def load(self, file):
        with open(file, 'r') as file_in:
            file_in.readlines(shapes)


class Square(Shape):
    def __init__(self, x, y, side):
        Shape.__init__(self, x, y)
        self.x = x
        self.y = y
        self.side = side

    def Show(self):
        print(f"Квадрат с координатами верхней левой точки ({self.x}, {self.y}) и длиной стороны {self.side}")


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        Shape.__init__(self, x, y)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def Show(self):
        print(f"Прямоугольник с координатами верхней левой точки ({self.x}, {self.y}), шириной {self.width} и высотой {self.height}")


class Circle(Shape):
    def __init__(self, x, y, radius):
        Shape.__init__(self, x, y)
        self.x = x
        self.y = y
        self.radius = radius

    def Show(self):
        print(f"Окружность с координатами центра ({self.x}, {self.y}) и радиусом {self.radius}")


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        Shape.__init__(self, x, y)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def Show(self):
        print(f"Эллипс с координатами верхнего левого угла ({self.x}, {self.y}), шириной {self.width} и высотой {self.height}")


a = Square(15, 15, 10)
b = Rectangle(20, 10, 15, 7)
c = Circle(11, 12, 10)
d = Ellipse(5, 15, 10, 5)

shapes = [Square(15, 15, 10), Rectangle(20, 10, 15, 7), Circle(11, 12, 10), Ellipse(5, 15, 10, 5)]


with open("shapes.txt", "wb") as file_in:
    file_in.readlines(shapes)


with open("shapes.txt", "rb") as file_out:
    file_out.writelines(shapes)


for shape in shapes:
    shape.Show()
