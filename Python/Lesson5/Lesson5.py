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
