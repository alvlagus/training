"""
1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
31 22 3 5 32 3 5 8 3
37 43 2 4 6 8 3 7 1
51 86 -1 64 -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

# class Matrix:
#     def __init__(self, data):
#         self.data = data
#
#     def __add__(self, other):
#         data = []
#         for j in range(len(self.data)):
#             data.append([])
#             for k in range(len(self.data[0])):
#                 data[j].append(self.data[j][k] + other.data[j][k])
#
#         return Matrix(data)
#
#     def __str__(self):
#         return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.data]))
#
#
# mx1 = Matrix([[1, 2, 3], [2, 3, 4], [2, 3, 4]])
# print(f'Первая матрица:\n{mx1}')
# print('-' * 10)
# mx2 = Matrix([[10, 10, 10], [10, 10, 10], [2, 3, 4]])
# print(f'Вторая матрица:\n{mx2}')
# print('-' * 10)
# print(f'Сумма матриц:\n{Matrix.__add__(self=mx1, other=mx2)}')


"""
2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property.
"""

# Вариант 1 с проверкой и без суммирования

# from abc import ABC, abstractmethod
#
#
# class Clothes(ABC):
#     name = None
#
#     @abstractmethod
#     def __init__(self):
#         self.__rast = None
#         self.__size = None
#
#     @abstractmethod
#     def __str__(self):
#         pass
#
#
# class Coat(Clothes, ABC):
#     name = 'пальто'
#
#     def __init__(self, size):
#         self.size = size
#
#     def __str__(self):
#         return
#
#     @property
#     def size(self):
#         return self.__size
#
#     @size.setter
#     def size(self, size):
#         if size < 40 or size > 64:
#             print(f'Введён некорректный размер')
#         else:
#             self.__size = size
#             print(f'На {self.name} {self.__size}-го размера требуется {round(self.__size / 6.5 + 0.5, 1)} метра(-ов)'
#                   f' ткани.')
#
#
# class Suit(Clothes, ABC):
#     name = 'костюм'
#
#     def __init__(self, rast):
#         self.rast = rast
#
#     def __str__(self):
#         return
#
#     @property
#     def rast(self):
#         return self.__rast
#
#     @rast.setter
#     def rast(self, rast):
#         if rast < 150 or rast > 220:
#             print(f'Введён некорректный рост')
#         else:
#             self.__rast = rast
#             print(f'На {self.name} {self.__rast}-го роста требуется {round(2 * self.__rast * 0.01 + 0.3, 1)} '
#                   f'метра(-ов) ткани.')
#
#
# coat = Coat(35)
# coat2 = Coat(60)
# suit = Suit(140)
# suit2 = Suit(160)


# Вариант 2 с суммированием по классам пальто и костюм

# from abc import ABC, abstractmethod
#
#
# class Clothes(ABC):
#     name = None
#
#     @abstractmethod
#     def __init__(self):
#         self.__rast = None
#         self.__size = None
#
#     @abstractmethod
#     def __str__(self):
#         pass
#
#     @abstractmethod
#     def __add__(self, other):
#         pass
#
#
# class Coat(Clothes, ABC):
#     name = 'пальто'
#
#     def __init__(self, size):
#         self.size = size
#
#     @property
#     def size(self):
#         return self.__size
#
#     @size.setter
#     def size(self, size):
#         if size < 40 or size > 64:
#             print(f'Введён некорректный размер')
#         else:
#             self.__size = size
#             print(f'На {self.name} {self.__size}-го размера требуется {round(self.__size / 6.5 + 0.5, 1)} метра(-ов)'
#                   f' ткани.')
#
#     def __add__(self, other):
#         try:
#             return round(self.__size / 6.5 + 0.5, 1) + round(other.__size / 6.5 + 0.5, 1)
#         except AttributeError:
#             return f'Введён некорректный размер'
#
#     def __str__(self):
#         return
#
#
# class Suit(Clothes, ABC):
#     name = 'костюм'
#
#     def __init__(self, rast):
#         self.rast = rast
#
#     @property
#     def rast(self):
#         return self.__rast
#
#     @rast.setter
#     def rast(self, rast):
#         if rast < 150 or rast > 220:
#             print(f'Введён некорректный рост')
#         else:
#             self.__rast = rast
#             print(f'На {self.name} {self.__rast}-го роста требуется {round(2 * self.__rast * 0.01 + 0.3, 1)} '
#                   f'метра(-ов) ткани.')
#
#     def __add__(self, other):
#         try:
#             return round(2 * self.__rast * 0.01 + 0.3, 1) + round(2 * other.__rast * 0.01 + 0.3, 1)
#         except AttributeError:
#             return f'Введён некорректный размер'
#
#     def __str__(self):
#         return
#
#
# coat = Coat(45)
# coat2 = Coat(55)
# suit = Suit(150)
# suit2 = Suit(160)
# print(f'Суммарное количество ткани на пошив пальто: {Coat.__add__(self=coat, other=coat2)} метра(-ов).')
# print(f'Суммарное количество ткани на пошив костюмов: {Suit.__add__(self=suit, other=suit2)} метра(-ов).')

"""
3) Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
количеству ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки 
арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только
к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением
до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n
равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод
make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод
make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""

# class Cell:
#     def __init__(self, size):
#         self.size = int(size)
#
#     def __str__(self):
#         return self.size * "*"
#
#     def __add__(self, other):
#         return Cell(self.size + other.size)
#
#     def __sub__(self, other):
#         if (self.size - other.size) > 0:
#             return Cell(self.size - other.size)
#         else:
#             return f'Разность количества ячеек двух клеток меньше нуля'
#
#     def __mul__(self, other):
#         return Cell(self.size * other.size)
#
#     def __truediv__(self, other):
#         return Cell(round(self.size // other.size))
#
#     def make_order(self, cells_in_row):
#         row = ''
#         for i in range(int(self.size / cells_in_row)):
#             row += f'{"*" * cells_in_row} \n'
#         row += f'{"*" * (self.size % cells_in_row)}'
#         return ''.join(row)
#
#
# cell1 = Cell(15)
# cell2 = Cell(6)
# print(f'Клетка 1: {cell1}')
# print(f'Клетка 2: {cell2}')
# print(f'Результат сложения клеток: {cell1 + cell2}')
# print(f'Результат вычитания клеток: {cell2 - cell1}')
# print(f'Результат умножения клеток: {cell1 * cell2}')
# print(f'Результат деления клеток: {cell1 / cell2}')
# print(f'Результат деления на столбцы клетки 1:\n{cell1.make_order(5)}')
