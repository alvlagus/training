"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
* Атрибут реализовать как приватный.
* В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый.
* Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
(зеленый) — на ваше усмотрение.
* Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый).
* Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.
"""

# from time import sleep
#
#
# class TrafficLight:
#     # атрибуты класса
#     color = 'цвет'
#
#     def running(self):
#         print(f'Светофор включён')
#         __color = 'Красный'
#         print(f'Загорелся  {__color}.')
#         sleep(7)
#         __color = 'Жёлтый'
#         print(f'Загорелся  {__color}.')
#         sleep(2)
#         __color = 'Зелёный'
#         print(f'Загорелся  {__color}.')
#         sleep(10)
#         print(f'Завершение цикла работы')
#
#
# inst1 = TrafficLight()
# inst1.running()


"""
2. Реализовать класс Road (дорога), в котором 
* определить атрибуты: length (длина), width (ширина). 
* Значения данных атрибутов должны передаваться при создании экземпляра класса. 
* Атрибуты сделать защищенными. 
* Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
* Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной 
в 1 см * число см толщины полотна. 
* Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т
"""

# class Road:
#     _length = None
#     _width = None
#
#     def __init__(self, _length=input('Введите длину дороги (м): '),
#                  _width=input('Введите ширину дороги (м): '),
#                  _unit_weight=input('Введите массу асфальта на 1 кв.м. дороги (кг): '),
#                  _thickness=input('Введите толщину слоя асфальта (см): ')):
#         self.length = _length
#         self.width = _width
#         self.unit_weight = _unit_weight
#         self.thickness = _thickness
#         try:
#             # Сразу кг переводим в т, а см в метры
#             weight = round(float(_length) * float(_width) * (float(_unit_weight) / 1000) * (float(_thickness) / 100), 1)
#             print(f'Необходимая масса асфальта  для устройства дорожного покрытия составляет: {weight} т')
#         except ValueError:
#             print(f'Введите число')
#
#
# road1 = Road()

"""
3. Реализовать базовый класс Worker (работник).
● определить атрибуты: name, surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
●
проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""

# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.n = name
#         self.s = surname
#         self.p = position
#         self._income = {"wage": wage, "bonus": bonus}
#
#
# class Position(Worker):
#     def __init__(self, name, surname, position, wage, bonus):
#         super().__init__(name, surname, position, wage, bonus)
#
#     def get_full_name(self):
#         return self.n + ' ' + self.s
#
#     def get_total_income(self):
#         return self._income.get('wage') + self._income.get('bonus')
#
#
# num1 = Position("Иван", "Петров", "сантехник", 25000, 1500)
# print(f'Работник: {num1.get_full_name()}')
# print(f'Должность: {num1.p}')
# print(f'Доход (с учётом премии): {num1.get_total_income()}')
# print('-' * 40)
#
# num2 = Position("Пётр", "Иванов", "водитель", 35000, 3000)
# print(f'Работник: {num2.get_full_name()}')
# print(f'Должность: {num2.p}')
# print(f'Доход (с учётом премии): {num2.get_total_income()}')
# print('-' * 40)
#
# num3 = Position("Ольга", "Сидорова", "кассир", 45000, 4500)
# print(f'Работник: {num3.get_full_name()}')
# print(f'Должность: {num3.p}')
# print(f'Доход (с учётом премии): {num3.get_total_income()}')
# print('-' * 40)


"""
4. Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
"""


# class Car:
#     def __init__(self, speed, color, name, is_police=False):
#         self._s = speed
#         self._c = color
#         self._n = name
#         self._i_p = is_police
#         if self._i_p is not False:
#             print(f'Машина полиции')
#
#     def go(self):
#         return f'Машина поехала'
#
#     def stop(self):
#         return f'Машина остановилась'
#
#     def turn(self, direction):
#         return f'Машина изменила направление {direction}'
#
#     def show_speed(self):
#         return f'Текущая скорость автомобиля {self._s}'
#
#     @property
#     def s(self):
#         return self._s
#
#     @property
#     def c(self):
#         return self._c
#
#     @property
#     def n(self):
#         return self._n
#
#
# class TownCar(Car):
#     def __init__(self, speed, color, name, is_police=False):
#         super().__init__(speed, color, name, is_police)
#
#     def show_speed(self):
#         if self._s > 60:
#             return f'Скорость превышена! \nЛимит скорости 60 км/ч.'
#         else:
#             return f'Текущая скорость автомобиля {self._s}'
#
#
# class SportCar(Car):
#     def __init__(self, speed, color, name, is_police=False):
#         super().__init__(speed, color, name, is_police)
#
#
# class WorkCar(Car):
#     def __init__(self, speed, color, name, is_police=False):
#         super().__init__(speed, color, name, is_police)
#
#     def show_speed(self):
#         if self._s > 40:
#             return f'Скорость превышена! \nЛимит скорости 40 км/ч.'
#         else:
#             return f'Текущая скорость автомобиля {self._s}'
#
#
# class PoliceCar(Car):
#     def __init__(self, speed, color, name, is_police=True):
#         super().__init__(speed, color, name, is_police)
#
#
# a = TownCar(70, "красная", "Audi", False)
# print(a.s)
# print(a.c)
# print(a.n)
# print(a.turn("направо"))
# print(a.show_speed())
# print("*" * 45)
# b = SportCar(110, "White", "BMW", False)
# print(b.s)
# print(b.c)
# print(b.n)
# print(b.turn("прямо"))
# print(b.show_speed())
# print("*" * 45)
# c = WorkCar(45, "Orange", "MAN", False)
# print(c.s)
# print(c.c)
# print(c.n)
# print(c.turn("налево"))
# print(c.show_speed())
# print("*" * 45)
# d = PoliceCar(70, "Blue", "Ford", True)
# print(d.s)
# print(d.c)
# print(d.n)
# print(d.turn("направо"))
# print(d.show_speed())

"""
5. Реализовать класс Stationery (канцелярская принадлежность).
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


# class Stationery:
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         return f'Запуск отрисовки'
#
#
# class Pen(Stationery):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def draw(self):
#         return f'Запуск отрисовки. Отрисовка производится ручкой {self.title}.'
#
#
# class Pencil(Stationery):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def draw(self):
#         return f'Запуск отрисовки. Отрисовка производится карандашом {self.title}.'
#
#
# class Handle(Stationery):
#     def __init__(self, title):
#         super().__init__(title)
#
#     def draw(self):
#         return f'Запуск отрисовки. Отрисовка производится маркером {self.title}.'
#
#
# kohinoor = Pencil("Koh-i-Noor")
# print(kohinoor.draw())
# parker = Pen("Parker")
# print(parker.draw())
# erichkrause = Handle("ErichKrause")
# print(erichkrause.draw())
