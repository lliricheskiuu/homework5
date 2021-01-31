# 1. Дано целое число (int). Определить сколько нулей в этом числе.

# 1)

# tmp = True
#
# while tmp:
#
#     try:
#         value = str(int(input("Enter your value:")))
#         print(value.count('0'))
#         tmp = False
#     except ValueError:
#         print("Enter int value!")

# 2)

# tmp = True
#
# while tmp:
#     try:
#         number = str(int(input('Enter your number:')))
#         tmp = False
#     except ValueError:
#         print("Enter int value!")
#
# count = 0
#
# for value in number:
#     if value == '0':
#         count += 1
# print(count)

# Попробывал решить двумя способами (1 - через .count; 2 - через цикл for и проверку на '0')

###

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа.

# number = str(int(input("Enter your number:")))
# count = 0
#
# for value in number[::-1]:
#     if value == '0':
#         count += 1
#     else:
#         break
#
# print(count)

###

# 3a. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

# my_list_1 = ['Q', 'w', 'e', 'r', 't', 'y']
# my_list_2 = ['y', 't', 'r', 'e', 'w', 'Q']
# my_result = []
#
# for index in range(len(my_list_1)):
#     if not index % 2:
#         my_result.append(my_list_1[index])
#
# for index in range(len(my_list_2)):
#     if index % 2:
#         my_result.append(my_list_2[index])
#
# print(my_result)

###

# 3b. Даны списки my_list_1 и my_list_2. Создать список my_result в который
# вначале поместить четные элементы (ИМЕННО ЭЛЕМЕНТЫ) из my_list_1 и потом нечетные элементы из my_list_2.
# my_list_1 = [1,3,2,4,5], my_list_2 = [10, 20, 15, 25, 22] -> my_result [2, 4, 15, 25]

# my_list_1 = [1, 5, 3, 2, 4, 4, 7, 8, 10, 100]
# my_list_2 = [2, 7, 5, 2, 2, 6, 3, 9, 7, 7, 10]
# my_result = []
#
# for value in my_list_1:
#     if not value % 2:
#         my_result.append(value)
#
# for value in my_list_2:
#     if value % 2:
#         my_result.append(value)
#
# print(my_result)

###

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

# my_list = [1, 2, 3, 4, 5]   # 2, 3, 4, 5, 1
# new_list = []

# 1)

# tmp = my_list[0]
#
# for index in range(len(my_list) - 1):
#     my_list[index] = my_list[index + 1]
# my_list[-1] = tmp
#
# new_list = my_list
# print(new_list)

# 2) удовлетворяет условию намного больше чем первый

# new_list = my_list[1:].copy()
# new_list.append(my_list[0])
# print(new_list)

###

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

# my_list = [1, 2, 3, 4, 5]   # 2, 3, 4, 5, 1

# 1)

# my_list.append(my_list[0])
# my_list.pop(0)
#
# print(my_list)

# 2)

# tmp = my_list[0]
# my_list.pop(0)
# my_list.append(tmp)
# print(my_list)

###

# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133.

# my_string = "43 больше чем 34 но меньше чем 56"
# my_string = my_string.split(' ')
#
# result = 0
#
# for value in my_string:
#     if value.isdigit():
#         value = int(value)
#         result += value
#
# print(result)

###

# 7. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']

# my_str = 'abcd'
# if not len(my_str) % 2:
#     my_str = my_str[:2] + ' ' + my_str[2:]
#     my_str = my_str.split()
#     print(my_str, type(my_str))
# else:
#     my_str = my_str[:2] + ' ' + my_str[2:]
#     tmp = my_str[-1]
#     my_str = my_str.replace(my_str[-1], '')
#     my_str = my_str + ' ' + tmp + '_'
#     my_str = my_str.split()
#     print(my_str)
# # знаю, что решил по хитрому, но я не знаю как по-другому

###

# 8. Дана строка my_str в которой символы не повторяются и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить часть строки между этими символами.
# my_str = "My_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"

# my_str = "My_long str"
# l_limit = "o"
# r_limit = "t"
#
# count_l = 0
# count_r = 0
#
# for symbol in my_str:
#     if not symbol == l_limit:
#         count_l += 1
#     else:
#         break
#
# for symbol in my_str:
#     if not symbol == r_limit:
#         count_r += 1
#     else:
#         break
#
# sub_str = my_str[count_l + 1:count_r]
# print(sub_str)

###
