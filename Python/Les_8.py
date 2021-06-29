"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
 преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
 и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

# class MyErr(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# class Data:
#     def __init__(self, value):
#         self.value = str(value)
#
#     @classmethod
#     def retrieval(cls, value):
#         today_data = value.split('-')
#         today_data = list(map(int, today_data))
#         return today_data
#
#
#     @staticmethod
#     def valid(day, month, year):
#         try:
#             if day < 1 or day > 31:
#                 raise MyErr(f'Дата {day}-{month}-{year} некорректна')
#             if month < 1 or month > 12:
#                 raise MyErr(f'Дата {day}-{month}-{year} некорректна')
#             if year < 0 or year > 2021:
#                 raise MyErr(f'Дата {day}-{month}-{year} некорректна')
#         except (NameError, ValueError, TypeError, MyErr) as err:
#             return f'{err}'
#         else:
#             return f'Дата {day}-{month}-{year} корректная'
#
#     def __str__(self):
#         return f'Текущая дата {Data.retrieval(self.value)}'
#
#
# today = Data('12-6-2021')
# print(today)
# print(Data.valid(12, 6, 2021))


"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, 
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать 
эту ситуацию и не завершиться с ошибкой.
"""

# class MyDiv(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# num1 = input('Введите число (делимое): ')
# num2 = input('Введите число (делитель): ')
# try:
#     n1 = float(num1)
#     n2 = float(num2)
#     if n2 == 0:
#         raise MyDiv(f'Деление на 0 запрещено')
# except (ValueError, MyDiv) as err:
#     print(err)
# else:
#     d = n1 / n2
#     print(f'Результат деления равен: {d}')

"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. 
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу 
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем 
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число. 
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. 
При этом работа скрипта не должна завершаться.
"""

# class MyErr:
#     def __init__(self, *args):
#         self.my_list = []
#
#     def my_input(self):
#
#         while True:
#             try:
#                 new_el = int(input('Введите новый элемент: число или "stop" для выхода: ').lower())
#                 self.my_list.append(new_el)
#
#             except:
#                 print(f'Необходимо вводить числа')
#                 ex = input(f'Введите число или "stop" для выхода: ')
#                 if ex != 'stop':
#                     print(a.my_input())
#                 else:
#                     print(f'\nТекущий список - {self.my_list}')
#                     return f'Выход'
#
#
# a = MyErr()
# print(a.my_input())


"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», 
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, 
уникальные для каждого типа оргтехники.
"""


# class Warehouse:
#     def __init__(self, name):
#         self.name = name
#         self.items = []
#
#     def __str__(self):
#         warehouse_status = f'Состояние склада "{self.name}":\n'
#         if self.items:
#             for i, item in enumerate(self.items):
#                 warehouse_status += f"{i}: {item}\n"
#         else:
#             warehouse_status += 'пусто!\n'
#         return warehouse_status
#
#     def receipt(self, equipment):
#         self.items.append(equipment)
#
#     def departure(self, equipment):
#         if not equipment in self.items:
#             raise KeyError(equipment)
#         self.items.remove(equipment)
#
#     def moving(self, equipment, another_warehouse):
#         self.departure(equipment)
#         another_warehouse.receipt(equipment)
#
#
# class OfficeEquipment:
#     def __init__(self, brand, model, price, color):
#         if not ((type(price) is int or type(price) is float) and price > 0):
#             raise ValueError('Цена должна быть положительным числом')
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.color = color
#         self.my_unit = {'Тип устройства': self.item_name,
#                         'Марка': self.brand,
#                         'Модель': self.model,
#                         'Цена за ед (₽)': self.price,
#                         'Цвет': self.color}
#
#     def __str__(self):
#         return f'{self.my_unit}'
#
#
# class Printer(OfficeEquipment):
#     item_name = 'Принтер'
#
#
# class Scanner(OfficeEquipment):
#     item_name = 'Сканер'
#
#
# class Copier(OfficeEquipment):
#     item_name = 'Копир'
#
#
# unit_1 = Printer("HP", "ХХХ", 1000, "черный")
# unit_2 = Scanner("Canon", "ННН", 2500, "белый")
# unit_3 = Copier("Xerox", "YYY", 4500, "красный")
# # print(unit_1)
# # print(unit_2)
# # print(unit_3)
#
# warehouse_main = Warehouse('main')
# warehouse_division_1 = Warehouse('Division_1')
# warehouse_division_2 = Warehouse('Division_2')
#
# warehouse_main.receipt(unit_1)
# warehouse_main.receipt(unit_2)
# warehouse_main.receipt(unit_3)
#
# print(warehouse_main)
#
# warehouse_main.moving(unit_1, warehouse_division_1)
#
# print(warehouse_main)
#
# warehouse_main.moving(unit_2, warehouse_division_2)
#
# print(warehouse_main)
#
# warehouse_main.moving(unit_3, warehouse_division_2)
#
# print(warehouse_main)

"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в 
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других 
данных, можно использовать любую подходящую структуру, например словарь.
"""

"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, 
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных 
на уроках по ООП.
"""

"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку 
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) 
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


# class ComplexNumber:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
#
#     def __add__(self, other):
#         return ComplexNumber(self.real + other.real, self.imag + other.imag)
#
#     def __mul__(self, other):
#         return ComplexNumber(self.real * other.real - self.imag * other.imag,
#                              self.imag * other.real + self.real * other.imag)
#
#     def __str__(self):  # Вывод на печать с учётом требований к записи комплексных чисел
#         sign = '+' if self.imag >= 0 else ''
#         if self.imag == 0:
#             return '{}'.format(self.real)
#         else:
#             return '{}{}{}j'.format(self.real, sign, self.imag)
#
#
# comp_num1 = ComplexNumber(2, 2)
# comp_num2 = ComplexNumber(1, 2)
# print(f'Первое комплексное число comp_num1 = {comp_num1}')
# print(f'Второе комплексное число comp_num2 = {comp_num2}')
# print(f'Сумма comp_num1 + comp_num2 = {comp_num1 + comp_num2}')
# print(f'Произведение comp_num1 * comp_num2 = {comp_num1 * comp_num2}')
