"""УРОК 1"""
# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел
# и строк и сохраните в переменные, выведите на экран.
# a = 7
# b = 2
# print("Первая переменная a=", a, ",", "Вторая переменная b=", b)
# print("Операции с переменными:")
# print("a + b =", a + b)
# print("a - b =", a - b)
# print("a * b =", a * b)
# print("a / b =", a / b)
# print("a // b =", a // b)
# print("a % b =", a % b)
# print("a ** b =", a ** b)
#
# name1 = input("Введите ваше имя: ")
# name2 = input("Введите вашу фамилию: ")
# year_birth = int(input("Введите ваш год рождения: "))
# year = int(input("Какой сегодня год? "))
# age = year - year_birth
# print("Введеные значения - %5s %5s %5d %5d" % (name1, name2, year_birth, year))
# print(f"Здравствуйте, {name1} {name2}!")
# print(f"Сейчас Вам {age} лет")

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

# Мой вариант
# user_time = int(input("Введите время в секундах: "))
# hours = user_time // 3600
# minutes = (user_time % 3600) // 60
# seconds = user_time % 60
# print(f"Время в формате чч:мм:сс {hours} : {minutes} : {seconds}")

# Решение проподавателя
# s = int(input('Введите время в секундах'))
# h = s // 3600
# m = (s - h * 3600) // 60
# sec = s % 60
# print(f'{h:02}:{m:02}:{sec:02}')

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

# Мой вариант
# n = input("Введите число: ")
# nn = int(n * 2)
# nnn = int(n * 3)
# n = int(n)
# #print(n, nn, nnn)
# print(n + nn + nnn)

# Вариант преподавателя
# n = input('Введите число: ')
# print(int(n) + int(n + n) + int(n + n + n))

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.

# Мой вариант
# number = abs(int(input("Введите целое положительное число: ")))  # исключаем отрицательные
# max_digit = number % 10  # предположение, что первая цифра (справа) максимальная
# while number > 0:  # условие, что оставшееся число больше 0
#     number = number // 10  # отбрасываем следующую цифру
#     if number % 10 > max_digit:  # проверка, что следующая цифра больше предыдущей
#         max_digit = number % 10   # если условие выполняется, меняем макс цифру
#     if number > 9:
#         continue
#     else:
#         print("Максимальное цифра в числе ", max_digit)
#         break

# Решение проподавателя
# num = int(input("Введите число: "))
# max1 = 0
# while num > 0:
#     last_dig = num % 10
#     if last_dig > max1:
#         max1 = last_dig
#         if max1 == 9:
#             break
#     num //= 10
# print('Максмальная цифра в числе - ', max1)


# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

# Мой вариант
# proceeds = p = int(input('Введите значение выручки: '))  # выручка
# costs = c = int(input('Введите значение издержек: '))  # издержки
# fin_result = fr = p - c  # прибыль
# if fin_result > 0:
#     print('Фирма работает в прибыль')
#     profitability = r = (fr / p) * 100  # рентабельность
#     print(f'Рентабельность выручки составляет {r}')
#     staff = s = int(input('Укажите число сотрудников: '))  # число сотрудников
#     print(f'Прибыль на одного сотрудника составляет {fr / s}')
# else:
#     print('Фирма работает в убыток')

# Решение проподавателя
# tr = float(input('Введите вашу выручку: '))
# tc = float(input('Введите ваши издержки: '))
# p = tr - tc
# if p > 0:
#     print('Вы получили приыль')
#     print('Рентабельность: ', p / tr)
#     i = int(input('Введите количество сотрудников: '))
#     print('Прибыль на одного сотрудника', p / i)
# elif p == 0:
#     print('Вы получили нулевую прибыль')
# else:
#     print('Вы работаете в убыток')

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

# Мой вариант
# a = int(input('Введите число а: '))
# b = int(input('Введите число b: '))
# if a <= 0 or b <= 0:
#     print('Введите положительные числа')
# else:
#     c = 1
#     while a < b:
#         c += 1
#         a = a + a * 0.1
#     print(f'На {c}-й день спортсмен достиг результата - пробежал не менее {b} км.')

# Решение проподавателя
# a = int(input('Введите число а: '))
# b = int(input('Введите число b: '))
# days = 1
# print('Результат: ')
# while a < b:
#     print(f'{days}-й день: {round(a, 2)}')
#     a = a * 1.1
#     days += 1
# print(f'на {days}-й день спортсмен достиг результата - не менее {b}  км')

"""УРОК 2"""

"""
1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
"""
# Мой вариант
# my_list = [2, 'text', 456, 45.3, [1, 2, 3], None, True]
# print(my_list)
# print(list(map(type, my_list)))

# Решение преподавателя
# li = [12, 8.0, True, [4, 7], (12, 'st'), 'hello', {'Alex': 1234}]
# for el in li:
#     print(f'{el} имеет тип: {type(el)}')

"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
элементов необходимо использовать функцию input().
"""
# Мой вариант
# list2 = []  # заводим пустой список
# n = int(input("Введите количество элементов списка: "))  # задаём количество элемент в списке
# # второй вариатн через while, как на уроке (1:28)
# for i in range(n):
#     list2.append(input())
# print("Исходный список: ", list2)
# i = 1
# while i < len(list2):
#     list2[i], list2[i-1] = list2[i-1], list2[i]
#     # print(list2)
#     i += 2
# print("Итоговый список: ", list2)


# Решение преподавателя

# li = input('Введите список через пробел: ').split()
# for i in range(1, len(li), 2):
#     li[i - 1], li[i] = li[i], li[i - 1]
# print(li)

# li = input('Введите список через пробел: ').split()
# for i in range(1, len(li), 2):
#     li.insert(i - 1, li.pop(1))
# print(li)
"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""
# Мой вариант
# # Решение через list
# # Разбиваем год по временам года в виде списков
# li_winter = [1, 2, 12]
# li_spring = [3, 4, 5]
# li_summer = [6, 7, 8]
# li_autumn = [9, 10, 11]
# a = int(input("Введите номер месяца от 1 до 12: "))
# if a in li_winter:
#     print("Это зима")
# elif a in li_spring:
#     print("Это весна")
# elif a in li_summer:
#     print("Это лето")
# elif a in li_autumn:
#     print("Это осень")
# else:
#     print("Введите число от 1 до 12!")
#
# # Решение через dict
# d_winter = {"jan": 1, "feb": 2, "dec": 12}
# d_spring = {"mar": 3, "apr": 4, "may": 5}
# d_summer = {"jun": 6, "jul": 7,"aug": 8}
# d_autumn = {"sep": 9, "oct": 10,"nov": 11}
# num = int(input("Введите номер месяца от 1 до 12: "))
# for el in d_winter:
#     if num == d_winter[el]:
#         print("Это зима")
# for el in d_spring:
#     if num == d_spring[el]:
#         print("Это весна")
# for el in d_summer:
#     if num == d_summer[el]:
#         print("Это лето")
# for el in d_autumn:
#     if num == d_autumn[el]:
#         print("Это осень")
# else:
#     print("Введите число от 1 до 12!")


# Решение преподавателя

# mon = int(input('Введите месяц: '))
# season_d = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
# season_l = ['Зима', 'Весна', 'Лето', 'Осень']
#
# for el in season_d:
#     if mon in season_d[el] and 0 < mon < 13:
#         print(f'{mon}й месяц - это {el}')
#
# if mon in [12, 1, 2]:
#     print(f'{mon}й месяц - это {season_l[0]}')
# elif mon in [3, 4, 5]:
#     print(f'{mon}й месяц - это {season_l[1]}')
# elif mon in [6, 7, 8]:
#     print(f'{mon}й месяц - это {season_l[2]}')
# elif mon in [9, 10, 11]:
#     print(f'{mon}й месяц - это {season_l[3]}')
# else:
#     print('Такого месяца нет')


"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""
# Мой вариант
# s = input('Введите строку из нескольких слов, разделённых пробелами: ')
# li_3 = s.split(' ')
# for i, v in enumerate(li_3, 1):
#     print(i, v[:10])  # ограничиваем длину выводимых слов с помощью среза


# Решение преподавателя
# st = input('Введите строку через пробел: ').split()
# for i, word in enumerate(st, 1):
#     print(i, word[:10])


"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""
# Мой вариант
# my_list = [7, 5, 3, 3, 2]
# print(f'Исходный рейтинг - {my_list}')
# new_el = int(input('Введите новый элемент или 888 для выхода: '))
# while new_el != 888:
#     for el in range(len(my_list)):
#         if my_list[el] == new_el:
#             my_list.insert(el + 1, new_el)
#             break
#         elif new_el > my_list[0]:
#             my_list.insert(0, new_el)
#         elif new_el < my_list[-1]:
#             my_list.append(new_el)
#         elif my_list[el] > new_el > my_list[el + 1]:
#             my_list.insert(el + 1, new_el)
#     print(f'Текущий рейтинг - {my_list}')
#     new_el = int(input('Введите новый элемент или 888 для выхода: '))


# Решение преподавателя

# li = [7, 5, 3, 3, 2]
# num = int(input('Введите число: '))
# i = 0
# for el in li:
#     if num <= el:
#         i += 1
# li.insert(i, num)
# print(li)


"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
# Мой вариант
# goods = []
# goods_feat = {'название': '', 'цена': '', 'количество': '', 'ед.': ''}
# analytics = {'название': [], 'цена': [], 'количество': [], 'ед.': []}
# num = 0
# goods_feat_ = None
# control = None
# while True:
#     control = input('Для выхода введите "Q", для продолжения "Enter", для вывода аналитики введите "A"').upper()
#     if control == 'Q':
#         break
#     num += 1
#     if control == 'A':
#         print(f'\n Аналитика: \n')
#         for k, v in analytics.items():
#             print(f'{k} : {v} \n')
#     for f in goods_feat.keys():
#         goods_feat_ = input(f'Введите "{f}":')
#         goods_feat[f] = int(goods_feat_) if (f == 'price' or f == 'quantity') else goods_feat_
#         analytics[f].append(goods_feat[f])
#     goods.append((num, goods_feat))
# print(f'\n Структура товаров:', *goods, sep='\n')


# Решение преподавателя


# params = {'название': '', 'цена': '', 'количество': '', 'ед.': ''}
# res = {'название': [], 'цена': [], 'количество': [], 'ед.': []}
# cort = []
# i = 0
# while True:
#     if input('Если хотите завершить программу, введите stop ').capitalize() == 'Stop':
#         break
#     i += 1
#     params = params.copy()
#     for el in params:
#         n = input(f'Введите данные - {el}: ')
#         params[el] = int(n) if n == 'цена' or n == 'количество' else n
#         res[el].append(params[el])
#     cort.append((i, params))
#     print(cort)
#
# for key, value in res.items():
#     print(f'{key}: {value}')

"""УРОК 3"""

"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

# def my_div(arg1, arg2, a='Деление на 0 запрещено!'):
#     if arg2 == 0:
#         try:
#             print(arg1 / 0)
#         except ZeroDivisionError:
#             print('Error')
#             return a
#     div = arg1 / arg2
#     print('Результат деления первого числа на второе: ')
#     return div
#
#
# print(my_div(arg1=float(input("Укажите первое число: ")), arg2=float(input("Укажите второе число: ")),
#              a='Деление на 0 запрещено!'))

# teacher variant


# def div(s1, s2):
#     try:
#         s1, s2 = int(s1), int(s2)
#         res = s1 / s2
#     except ValueError:
#         return "Not a number"
#     except ZeroDivisionError:
#         return "Can't divide by zero"
#     return res
#
#
# a = input('Num 1: ')
# b = input("Num 2: ")
# print(div(a, b))

"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные 
аргументы. Реализовать вывод данных о пользователе одной строкой.
"""

"""
Переменные:
first_name - имя
second_name - фамилия
year - год рождения
city - город проживания
email -  email
phone - телефон
"""

# def my_func(first_name, second_name, year, city, email, phone):
#     res = f'\n Данные о пользователе: \n Имя пользователя: {first_name}; \n Фамилия пользователя {second_name}; \n ' \
#           f'Год рождения: {year};\n Город проживания: {city};\n Адрес электронной почты: {email};\n ' \
#           f'Номер телефона: {phone}.'
#     return res
#
#
# print(my_func(first_name=input('Введите ваше имя: '), second_name=input('Введите вашу фамилию: '),
#               year=input('Введите год рождения: '), city=input('Введите город проживания: '),
#               email=input('Введите адрес электронной почты: '), phone=input('Введите номер телефона: ')))


# teacher variant

# def info(name, surn, birth, city, email, tel):
#     return f'Name: {name}, Surname: {surn}, Birthday: {birth}, City: {city}, email: {email}, tel: {tel}'
#
#
# print(info(name=input('Введите ваше имя: '), surn=input('Введите вашу фамилию: '),
#            birth=input('Введите год рождения: '), city=input('Введите город проживания: '),
#            email=input('Введите адрес электронной почты: '), tel=input('Введите номер телефона: ')))

"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
аргументов.
"""

# def my_func(var_1, var2, var3):
#     list3 = [var_1, var2, var3]
#     list3.sort(reverse=True)
#     res = list3[0] + list3[1]
#     return res
#
#
# print('Сумма наибольших двух аргументов:', my_func(45.4, 30, 50))


# teacher variant

# 3.1
# def exc_min(a, b, c):
#     li = [a, b, c]
#     try:
#         li.remove((min(li)))
#         return sum(li)
#     except TypeError:
#         return 'Not a number'
#
#
# print(exc_min(9, 12, 3))

# 3.2
# def exc_min2(a, b, c):
#     try:
#         res = sum(sorted([a, b, c])[1:])
#         return res
#     except TypeError:
#         return 'Not a number'
#
#
# print(exc_min2(1, 7, 10))


"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""
"""
Действительными или вещественными числами называются все положительные числа, отрицательные числа и нуль.
Целыми числами называются все натуральные числа, все числа противоположные им по знаку и нуль.
"""

# def my_func():
#     x = abs(float(input("Укажите действительное положительное число X: ")))
#     y = (abs(int(input("Укажите отрицательное число Y: "))) * (-1))
#     a = 'Y не должен быть нулём'
#     if y == 0:
#         return a
#     res = x ** y
#     return res
#
#
# print(my_func())

# def my_func():
#     x = abs(float(input("Укажите действительное положительное число X: ")))
#     y = abs(int(input("Укажите отрицательное число Y: ")))
#     a = 'Y не должен быть нулём'
#     if y == 0:
#         return a
#     i = 1
#     res = 1
#     while i <= y:
#         res /= x
#         i += 1
#     return res
#
#
# print(my_func())


# teacher variant
# 4.1
# def my_pow(x, y):
#     try:
#         res = x ** y
#         return res
#     except TypeError:
#         return 'Not a number'
#
# print(my_pow(2, -3))

# 4.2
# def my_pow2(x, y):
#     try:
#         x, y = float(x), int(y)
#         res = 1
#         for _ in range(abs(y)):
#             res /= x
#         return round(res, 7)
#     except ValueError:
#         return 'Not a number'
#
# num1 = input('x: ')
# num2 = input('y: ')
#
# print(my_pow2(num1, num2))

"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться 
сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. 
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный 
символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно 
добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

# def my_func():
#     ext = False
#     res = 0
#     while not ext:
#         arg = input(f'Введите числа через пробел. Для вывода промежуточной суммы, нажмите Enter или Q для выхода: ')
#         str_list = arg.split()  # преобразовываем строку в список
#         sum_list = 0
#         for el in range(len(str_list)):
#             if str_list[el] == 'q' or str_list[el] == 'Q':  # проверка на анличие спецсимвола Q
#                 ext = True
#                 break
#             else:
#                 sum_list += float(str_list[el])  # либо int() для целых чисел
#         res += sum_list
#         print(f'Текущая сумма: {res}')
#
#     print(f'Конечная сумма: {res}')
#
#
# my_func()


# teacher variant

# def summ():
#     res = 0
#     while True:
#         li = input('Введите число через пробел, для выхода - stop ').split()
#         for num in li:
#             if num == 'stop':
#                 return  res
#             else:
#                 try:
#                     res += int(num)
#                 except ValueError:
#                     print('Для выхода - stop')
#         print('Summa = ', res)
#
#
# print(summ())

"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной 
первой буквой. Например, print(int_func(‘text’)) -> Text.
"""

# def int_func(w):
#     ext_w = w.capitalize()
#     return ext_w
#
#
# print(int_func(input(f'Введите слово: ')))

# teacher variant
# см. задачу № 7

"""
7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово
состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с
заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""


# Var_1
# def int_new_func(s):
#     ext_w = s.title()
#     return ext_w
#
#
# print(int_new_func(input(f'Введите строку из слов через пробел: ')))

# var_2
# def int_new_func():
#     s = input(f'Введите строку из слов через пробел: ').split()
#     for el in s:
#         def int_func(el):
#             ext_w = el.capitalize()
#             return ext_w
#
#         print(int_func(el))
#
#
# print(int_new_func())


# teacher variant

# def int_func():
#     li = input('Введите слова через пробел: ').split()
#     for word in li:
#         lenn = 0
#         for ch in word:
#             if 97 <= ord(ch) <= 122:
#                 lenn += 1
#         if lenn == len(word):
#             print(word.title())
#         else:
#             print(f'Ошибка: {word} - допустим только нижний регистр')
#
#
# int_func()

"""УРОК 4"""

"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета
для конкретных значений необходимо запускать скрипт с параметрами.

"""

# from sys import argv
# try:
#     working_out, rate, prize = map(int, argv[1:])
#     wage = (working_out * rate + prize)
#     print(f'Название - {argv[0]}')
#     print(f'Выработка - {argv[1]}')
#     print(f'Ставка в час - {argv[2]}')
#     print(f'Премия - {argv[3]}')
#     print(f'Заработная плата сотрудника равна: {wage}')
# except ValueError:
#     print(f'Введите число')

# Под Ubuntu через терминал PyCharm проверял по команде python3 Lesson4.py 8 100 50
# Название - Lesson4.py
# Выработка - 8
# Ставка в час - 100
# Премия - 50
# Заработная плата сотрудника равна: 850

# teacher variant

# from sys import argv
# def salary(hours, rate, premium):
#     try:
#         hours, rate, premium = map(float, argv[1:])
#         print('Зарплата: ', hours * rate * premium)
#     except:
#         print('Запустите скрипт с тремя параметрами: часы, ставка в час и премия')
#
#
# salary(8, 100, 150)

# Скрипт не работает. Скорее всего при дополнении прийдём к моему варианту


'''
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''
# original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# new_list = [original_list[i+1] for i in range(len(original_list)-1) if original_list[i] < original_list[i+1]]
# print(f'Исходный список: {original_list}')
# print(f'Итоговый список: {new_list}')

# teacher variant
# li = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# new = [li[i] for i in range(1, len(li)) if li[i] > li[i - 1]]
# print(new)

'''
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
'''

# new_list = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]  # 240 включается в список
# print(new_list)

# teacher variant
# lu2 = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
# print(lu2)

'''
4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел, 
соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. 
Для выполнения задания обязательно использовать генератор. 
Пример исходного списка: 
[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
'''

# old_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# new_list = [el for el in old_list if old_list.count(el) == 1]  #  находим количество повторений методом count()
# print(new_list)

# teacher variant
# li = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# new = [i for i in li if li.count(i) == 1]
# print(new)
'''
5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные 
числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

# from functools import reduce
#
# li = [el for el in range(100, 1001) if el % 2 == 0]  # 1000 включается в список
#
#
# def my_func(prev_el, el):
#     # prev_el - предыдущий элемент
#     # el - текущий элемент
#     return prev_el * el
#
#
# print(reduce(my_func, li))

# teacher variant

# from functools import reduce
# new = [el for el in range(100, 1001, 2)]
# print(new)
#
# def multiplication(arg1, arg2):
#     return arg1 * arg2
#
#
# print(reduce(multiplication, new))

'''
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. 
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
'''
# а) итератор, генерирующий целые числа, начиная с указанного,
# Ошибка. Нет приглашения на ввод данных

# from sys import argv
# from itertools import count
#
# try:
#     num, repeat_num = map(int, argv[1:])
#     for el in count(num):
#         if el > repeat_num:
#             break
#         else:
#             print(el)
# except ValueError:
#     print(f'Введите число')

# б) итератор, повторяющий элементы некоторого списка, определенного заранее
# from sys import argv
# from itertools import cycle
# path, my_value, repeat_value = argv
# c = 0
# for el in cycle(argv[1]):
#     if c > int(argv[2]):
#         break
#     print(el)
#     c += 1

# teacher variant

# 6.1

# from itertools import cycle, count
# st = int(input('Введите начальное число: '))
# end = int(input('Введите конечное число: '))
# for i in count(st):
#     print(i)
#     if i == end:
#         break

# 6.2

# from itertools import cycle
#
# li = input('Введите список через пробел: ').split()
#
# for el in cycle(li):
#     stop = input('Итерируемся дальше? Для выхода введите "нет" ')
#     if stop.title() == 'нет':
#         break
#     print(el)


'''
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
 должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает
  за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''


# n = int(input('Введите число: '))
#
#
# def fact():
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#         yield fact
#
#
# g = fact()
# c = 0
# for i in g:
#     if c < n:
#         print(i)
#         c += 1
#     else:
#         break

# teacher variant


# def fact(b):
#     res = 1
#     if b == 0:
#         yield f'{b}! = 1'
#     for i in range(1, b + 1):
#         res *= i
#         yield f'{i}! = {res}'
#
#
# n = int(input('Введите число, максимальный факториал которого хотите получить: '))
# for el in fact(n):
#     print(el)

"""УРОК 5"""

"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
# with open('text1.txt', 'w', encoding='utf-8') as f_obj:
#     ext = False
#     res = 0
#     while not ext:
#         n = input('Введите текст или пустую строку для выхода: ')
#         if n == '':
#             ext = True
#             break
#         else:
#             print(n, file=f_obj)

# teacher variant

# with open('text1.txt', 'w', encoding='utf8') as f:
#     line = ' '
#     while line != '':
#         line = input()
#         print(line, file=f)

"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, 
количества слов в каждой строке.
"""

# try:
#     with open("text2.txt") as f_obj:
#         line_count = 0
#         for line in f_obj:
#             print(line, end='')
#             line_count += 1
#     print('-' * 40)
#     print(f'Количество строк в документе: {line_count}.')
#     print('-' * 40)
#     with open("text2.txt") as f_obj:
#         content = f_obj.readlines()
#         # print(content)
#         # print('-' * 40)
#         words_count = ''
#         i = 0
#         for el in content:  # Считал знаки припинания (":", ",", ".") вместе со словами. Знак "-" также подсчитан
#             words_count = len(el)
#             lst = el.split()
#             words_count = len(lst)
#             i += 1
#             print(f'Количество  слов в строке {i}: {words_count}.')
# except IOError:
#     print("Произошла ошибка ввода-вывода!")

# teacher variant

# with open('text2.txt', 'r', encoding='utf8') as f:
#     text = f.readlines()
#     for i , line in enumerate(text, 1):
#         words = len(line.split())
#         print(f'{i}-ая строка содержит {words} слов')

"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
"""
# try:
#     with open("text3.txt") as f_obj:
#         payroll = f_obj.read().split('\n')
#         print(payroll)
#         poor = []
#         salary = []
#         for i in payroll:
#             i = i.split()
#             if float(i[1]) < 20000:
#                 poor.append(i[0])
#             salary.append(i[1])
#         average_salary = sum(map(float, salary)) / len(salary)
#     print(f'Оклад менее 20 тыс. рублей имеют: {poor}. \nСредний доход сотрудников {average_salary} рублей.')
# except IOError:
#     print("Произошла ошибка ввода-вывода!")

# teacher variant

# total_w = 0
# empl = 0
# with open('text3.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         total_w += float(line.split()[1])
#         empl += 1
#         if float(line.split()[1]) < 20000:
#             print(line.split()[0])
# print('Средняя величина дохода: ', round(total_w / empl, 2))


"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый 
текстовый файл.
"""

# try:
#     with open('text4.txt') as f_obj:
#         s = f_obj.read().split('\n')
#         new_s = []
#         print(f'Исходный текст:  {s}')
#         rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
#         for i in s:
#             i = i.split(' ', 1)
#             new_s.append(rus[i[0]] + '  ' + i[1])
#         print(f'Итоговый текст:  {new_s}')
#     with open('text4_new.txt', 'w') as new_f_obj:
#         print(new_s, file=new_f_obj)
# except IOError:
#     print("Произошла ошибка ввода-вывода!")

# teacher variant

# dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
#
# with open('text4_new.txt', 'w', encoding='utf-8') as f_write:
#     with open('text4.txt', 'r', encoding='utf-8') as f_read:
#         for line in f_read:
#             f_write.writelines([line.replace(line.split()[0], dic[line.split()[0]])])

"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

# try:
#     with open('text5.txt', 'w+', encoding='utf-8') as f_obj:
#         print('10 15 25 36', file=f_obj)
#         f_obj.seek(0)
#         content = f_obj.read().split()
#         sum_content = sum(map(int, content))
#         print(f'Сумма чисел равна: {sum_content}')
# except IOError:
#     print("Произошла ошибка ввода-вывода!")

# teacher variant

# from random import randint
#
# with open('text5.txt', 'w', encoding='utf-8') as f:
#     li = [randint(1, 20) for _ in range(50)]
#     f.write(' '.join(map(str, li)))
#
# print('Сумма чисел: ', sum(li))

"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
 практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
  были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
  Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

# a_dict = {}
# try:
#     with open('text6.txt') as f_obj:
#         content = f_obj.readlines()
#         print(content)
#         for line in content:
#             s = line.replace('(', ' ').split()
#             # print(s)
#             a_dict[s[0][:-1]] = sum(int(i) for i in s if i.isdigit())
# except IOError:
#     print("Произошла ошибка ввода-вывода!")
# print(f'Общее количество занятий по предметам: \n{a_dict}')

# teacher variant
# with open('text6.txt', 'r', encoding='utf-8') as f:
#     text = f.readlines()
#     for line in text:
#         new = ''
#         for el in line:
#             new = ''.join([new, (el if el in '0123456789' else ' ')])
#         res = [int(i) for i in new.split()]
#         print(f'{line.split()[0]} - {sum(res)} часов')


"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, 
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
 убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
 Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

# import json
#
# sum_profit = []
# dict_profit = {}
# dict_ap = {}
# total_list = []
#
# try:
#     with open('text7.txt') as f_obj:
#         my_li = f_obj.readlines()
#         print(f'Исходный список: {my_li}')
#         for i in my_li:
#             i = i.split()
#             profit = float(i[2]) - float(i[3])  # расчёт прибыли
#             if profit > 0:
#                 sum_profit.append(i[2])
#             else:
#                 profit = float(i[2]) - float(i[3])  # расчитываем убыток, но не учитываем при расчёте средней прибыли
#             dict_profit[i[0]] = profit  # составляем словарь фирма - прибыль / убыток
#         average_profit = sum(map(float, sum_profit)) / len(sum_profit)  # средняя выручка
#         dict_ap = {'average_profit': average_profit}  # составляем словарь средняя прибыль : значение
#         total_list = [dict_profit, dict_ap]
#         print('-' * 50)
#         print(f'Средняя прибыль равна: {average_profit}')
#         print('-' * 50)
#         print(f'Словарь фирма: прибыль/убыток со знаком "-": {dict_profit}')
#         print('-' * 50)
#         print(f'Словарь средняя прибыль: значение: {dict_ap}')
#         print('-' * 50)
#         print(f'Итоговый список: {total_list}')
#         print('-' * 50)
#     with open("text7.json", "w") as write_f:
#         json.dump(total_list, write_f)
#     print(f'Итоговый список скопирован в файл text7.json')
# except IOError:
#     print("Произошла ошибка ввода-вывода!")

# teacher variant

# import json
#
# with open('text7.json', 'w', encoding='utf-8') as f_write:
#     with open('text7.txt', 'r', encoding='utf-8') as f_read:
#         profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_read}
#         res = [profit, {'average_profit': sum([int(i) for i in profit.values() if int(i) > 0]) /
#                                           len([int(i) for i in profit.values() if int(i) > 0])}]
#     json.dump(res, f_write)

"""УРОК 6"""

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

# teacher variant
# 1.1
# from time import sleep
#
#
# class TrafficLight:
#     __color = 'красный'
#
#     def running(self):
#         print('Светофор горит красным')
#         sleep(7)
#         print('Светофор горит жёлтым')
#         sleep(2)
#         print('Светофор горит зелёным')
#         sleep(3)
#
#
# traf_light = TrafficLight()
# traf_light.running()

# 1.2
# from time import sleep
#
#
# class TrafficLight:
#     __color = ['красный', 'жёлтый', 'зелёный']
#
#     def running(self):
#         print('Горит', self.__color[0])
#         sleep(7)
#         print('Горит', self.__color[1])
#         sleep(2)
#         print('Горит', self.__color[2])
#         sleep(3)
#
#
# traf_light = TrafficLight()
# traf_light.running()


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


# teacher variant
# class Road:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     def calc(self):
#         return f'Масса равна: {(self._length * self._width * 25 * 0.05) / 1000} т'
#
# road1 = Road(5000, 20)
# print(road1.calc())

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


# teacher variant
# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}
#
#
# class Position(Worker):
#     def get_full_name(self):
#         return f'{self.name} {self.surname}'
#
#     def get_full_profit(self):
#         return f'{sum(self._income.values())}'
#
#
# worker1 = Position("Иван", "Петров", "сантехник", 25000, 1500)
# print(worker1.get_full_name())
# print(worker1.get_full_profit())

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


# teacher variant


# class Car:
#     def __init__(self, name, color, speed, is_police=False):
#         self.name = name
#         self.color = color
#         self.speed = speed
#         self.is_police = is_police
#         print(f'Новая машина: {self.name} цвет: {self.color} полиция? {self.is_police}')
#
#     def go(self):
#         print(f'Машина {self.name} поехвала')
#
#     def stop(self):
#         print(f'Машина {self.name} остановилась')
#
#     def turn(self, direction):
#         print(f'Машина {self.name} повернула {"налево" if direction == 0 else "направо"}')
#
#     def show_speed(self):
#         print(f'Машина {self.name} едет со скоростью {self.speed}')
#
#
# class TownCar(Car):
#     def show_speed(self):
#         print(f'Машина {self.name} едет со скоростью {self.speed} {"Превышение скорости" if self.speed > 60 else "Скорость не привышена"}')
#
#
# class WorkCar(Car):
#     def show_speed(self):
#         print(f'Машина {self.name} едет со скоростью {self.speed} {"Превышение скорости" if self.speed > 40 else "Скорость не привышена"}')
#
#
# class SportCar(Car):
#     pass
#
#
# class PoliceCar(Car):
#     def __init__(self, name, color, speed, is_police=True):
#         super().__init__(name, color, speed, is_police)
#
#
# town_car = TownCar('Bus', 'yellow', 50)
# town_car.turn(0)
# town_car.show_speed()
#
# police_car = PoliceCar('Police', 'white', 120)
# police_car.stop()
# police_car.show_speed()
# print(police_car.is_police)

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


# teacher variant

# class Stationery:
#     def __init__(self, title='Может рисовать'):
#         self.title = title
#
#     def draw(self):
#         return f'Запуск отрисовки'
#
#
# class Pen(Stationery):
#     def draw(self):
#         print(f'Запуск отрисовки ручкой {self.title}')
#
#
# class Pencil(Stationery):
#     def draw(self):
#         print(f'Запуск отрисовки карандашом {self.title}')
#
#
# class Handler(Stationery):
#     def draw(self):
#         print(f'Запуск отрисовки маркером {self.title}')
#
#
# kohinoor = Pencil("Koh-i-Noor")
# kohinoor.draw()
# parker = Pen("Parker")
# parker.draw()
# erichkrause = Handler("ErichKrause")
# erichkrause.draw()

"""УРОК 7"""

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
#                 data[j].append(self.data[j][k] + other.data[j][k])#
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


# teacher variant

# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
#
#
# class Matrix:
#
#     def __init__(self, data):
#         self.data = data
#
#     """ 1 способ печати """
#     # def __str__(self):
#     #     return '\n'.join(map(str, self.data))
#
#     """ 2 способ печати """
#     def __str__(self):
#         return '\n'.join('\t'.join([str(it) for it in line]) for line in self.data)
#
#     def __add__(self, other):
#         new = []
#         for i in range(len(self.data)):
#             new.append([])
#             for j in range(len(self.data[0])):
#                 new[i].append(self.data[i][j] + other.data[i][j])
#         # return '\n'.join(map(str, new))  сразу в методе делаем печать
#         return Matrix(new)  # возвращем безымянный объект, к которому применится метод __str__ при использовании print()
#
#
# matr1 = Matrix(a)
# matr2 = Matrix(b)
# print(matr1)
# print(matr1 + matr2)

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


# teacher variant

# from abc import ABC, abstractmethod
#
# class Clothes(ABC):
#
#     def __init__(self):
#         pass
#
#     @property
#     @abstractmethod
#     def consumption(self):
#         pass
#
#     def __add__(self, other):
#         return self.consumption + other.consumption
#
#
# class Coat(Clothes):
#     def __init__(self, size):
#         super().__init__()
#         self.size = size
#
#     @property
#     def size(self, size):
#         return self.__size
#
#     @size.setter
#     def size(self, size):
#         if size < 40:
#             print('Минимальный размер 40')
#             self.__size = 40
#         elif size > 56:
#             print('Максимальный размер 56')
#             self.__size = 56
#         else:
#             self.__size = size
#
#     @property
#     def consumption(self):
#         return self.__size / 6.5 + 0.5
#
#
# class Costume(Clothes):
#     def __init__(self, height):
#         super().__init__()
#         self.height = height
#
#     @property
#     def height(self, height):
#         return self.__height
#
#     @height.setter
#     def height(self, height):
#         if height < 150:
#             print('Минимальный рост 150')
#             self.__height = 150
#         elif height > 220:
#             print('Максимальный рост 220')
#             self.__height = 220
#         else:
#             self.__height = height
#
#     @property
#     def consumption(self):
#         return self.__height / 100 * 2 + 0.3
#
#
# coat1 = Coat(int(input('Размер пальто: ')))
# print(f'Вам нужно {coat1.consumption:.2f} метров ткани для пальто')
# cost1 = Costume(int(input('Рост для костюма: ')))
# print(f'Вам нужно {cost1.consumption:.2f} метров ткани для костюма')
# print(f'Всего нужно {coat1 + cost1:.2f} метров ткани на пальто и костюм')



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


# teacher variant


# class Cell:
#     def __init__(self, num):
#         self.num = num
#
#     def __str__(self):
#         return f'{self.num}'
#
#     def __add__(self, other):
#         return Cell(self.num - other.num)
#
#     def __sub__(self, other):
#         if self.num - other.num > 0:
#             return Cell(self.num - other.num)
#         else:
#             print('Нельзя выполнить операцию вычитания')
#
#     def __mul__(self, other):
#         return Cell(self.num * other.num)
#
#     def __truediv__(self, other):
#         return Cell(self.num // other.num)
#
#     def make_order(self, rows):
#         return '\n'.join(['*' * rows for _ in range(self.num // rows)]) + '\n' + '*' * (self.num % rows)
#
# cell1 = Cell(12)
# cell2 = Cell(7)
# print(cell1 + cell2)
# print(cell1 * cell2)
# print(cell1.make_order(4))

"""УРОК 8"""

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

# teacher variant

# class Data:
#     def __init__(self, st):
#         Data.data = st.split('-')
#
#     @classmethod
#     def get_info(cls):
#         try:
#             day, month, year = map(int, cls.data)
#             return day, month, year
#         except ValueError:
#             return 'Not a number'
#
#     @staticmethod
#     def validation(obj):
#         day, month, year = obj.get_info()
#         if 0 <= day <= 31 and 0 <= month <= 12 and 0 <= year <= 2021:
#             print('it`s a valid data')
#         else:
#             print('it`s a not valid data')
#
#
# day1 = Data('12-03-2020')
# print(day1.get_info())
# Data.validation(day1)
#
# day2 = Data('12-24-2020')
# print(day2.get_info())
# Data.validation(day2)
#
# day3 = Data('12-03-2898')
# print(day3.get_info())
# Data.validation(day3)


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


# teacher variant

# class MyError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# num1 = input("Num1: ")
# num2 = input("Num2: ")
# try:
#     num1 = float(num1)
#     num2 = float(num2)
#     if num2 == 0:
#         raise MyError("Can`t divide by zero")
# except (ValueError, MyError) as err:
#     print(err)
# else:
#     print(round(num1 / num2, 3))


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

# teacher variant

# class MyError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# li = []
# while True:
#     el = input('Enter a number: ')
#     if el.title() == 'Stop':
#         break
#     try:
#         if not el.isdigit():
#             raise MyError('Not a number')
#         el = int(el)
#         li.append(el)
#     except MyError as err:
#         print(err)
#     print(f'Current list: {li}')
# print(f'Final list: {li}')

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


# teacher variant

# class Storage:
#     def __init__(self):
#         self.li_id = []
#         self.li_st = []
#
#     def get_inventory(self, obj, status):
#         if obj.id and obj.model:
#             self.li_id.append(obj.id)
#             self.li_st.append(status)
#
#     def get_status(self, obj):
#         if obj.id and obj.model:
#             print(f'Item with id: {obj.id} is {self.li_st[self.li_id.index(obj.id)]}\n')
#
#
# class Equipment:
#     def __init__(self, id, model):
#         self.id = id
#         self.model = model
#         try:
#             int(self.id)
#         except ValueError:
#             print(f'id {self.id} should be a number!\n')
#             self.id = None
#         else:
#             if self.model.title() in ['Printer', 'Copier', 'Scanner']:
#                 print(f'id: {self.id} is {self.model}')
#             else:
#                 print(f'{self.model} is unknown type of item\n')
#                 self.model = None
#
#
# class Printer(Equipment):
#     def __init__(self, id, model, is_color):
#         super().__init__(id, model)
#         self.is_color = is_color
#
# class Copier(Equipment):
#     def __init__(self, id, model, speed):
#         super().__init__(id, model)
#         self.speed = speed
#
# class Scanner(Equipment):
#     def __init__(self, id, model, resolution):
#         super().__init__(id, model)
#         self.resolution = resolution
#
#
# storage = Storage()
# printer1 = Printer('1264', 'Printer', True)
# storage.get_inventory(printer1, 'In storage')
# storage.get_status(printer1)
#
# scanner1 = Scanner('78d3', 'Scanner', '600*600')
# storage.get_inventory(scanner1, 'Dispatched')
# storage.get_status(scanner1)
#
# copier1 = Copier('9812', 'Copier', '5l/min')
# storage.get_inventory(copier1, 'Dispatched')
# storage.get_status(copier1)
#
# copier2 = Copier('1723', 'Copiiier', '5l/min')
# storage.get_inventory(copier2, 'Dispatched')
# storage.get_status(copier2)

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

# teacher variant


# class Complex:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         if self.b < 0:
#             return f"{self.a}{self.b}j"
#         return f"{self.a}+{self.b}j"
#
#     def __add__(self, other):
#         return Complex(self.a + other.a, self.b + other.b)
#
#     def __mul__(self, other):
#         return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)
#
#
# c1 = Complex(1, -2)
# c2 = Complex(0, 3)
# c3 = Complex(6, 4)
# print(f'Первое комплексное число comp_num1 = {c1}')
# print(f'Второе комплексное число comp_num2 = {c2}')
# print(c1 + c2 + c3)
# print(c2 * c3)
