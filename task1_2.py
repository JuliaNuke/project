# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень
# числа X):
# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 –
# делится нацело на 7. Внимание: использовать только арифметические операции!
# b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
# списка, сумма цифр которых делится нацело на 7.
# c. * Решить задачу под пунктом b, не создавая новый список.

# a
my_list = []
for i in range(1, 1001, 2):
    my_list.append(i ** 3)


def summa_numbers(number):
    sum_num = 0
    last_number = number % 10
    while last_number != 0:
        sum_num = sum_num + last_number
        number = number // 10
        last_number = number % 10
    return sum_num


summa_num = []

for i in my_list:
    ret_sum = summa_numbers(i)
    summa_num.append(ret_sum)

list7 = []

for i in summa_num:
    if i // 7:
        list7.append(i)

total_sum = 0

for i in list7:
    total_sum = total_sum + i

print(total_sum)

# b
my_list = []
for i in range(1, 1001, 2):
    my_list.append(i ** 3 + 17)


def summa_numbers(number):
    sum_num = 0
    last_number = number % 10
    while last_number != 0:
        sum_num = sum_num + last_number
        number = number // 10
        last_number = number % 10
    return sum_num


summa_num = []

for i in my_list:
    ret_sum = summa_numbers(i)
    summa_num.append(ret_sum)

list7 = []

for i in summa_num:
    if i // 7:
        list7.append(i)

total_sum = 0

for i in list7:
    total_sum = total_sum + i

print(total_sum)
