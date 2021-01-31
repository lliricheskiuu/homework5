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

my_list = [1, 2, 3, 4, 5]   # 2, 3, 4, 5, 1

# 1)

# my_list.append(my_list[0])
# my_list.pop(0)
#
# print(my_list)

# 2)

tmp = my_list[0]
my_list.pop(0)
my_list.append(tmp)
print(my_list)
