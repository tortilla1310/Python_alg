# Задание №4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов
# (n) вводится с клавиатуры.

elements_number = int(input('Введите количество символов для вывода '))

sum_of_elements = 0
for i in range(elements_number):
    sum_of_elements += 1 / pow(-2, i)
print('Сумма n элементов =', sum_of_elements)