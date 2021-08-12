# Задание №1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
# программах в рамках первых трех уроков. Проанализировать результат и определить программы
# с наиболее эффективным использованием памяти.

#3.2
from sys import getsizeof
from random import randint

length = 15
arr  = [0] * length
even = []

for i in range(length):
    arr[i] = randint(1, 40)
    if arr[i] % 2 == 0:
        even.append(arr[i])
print(f'Массив:', arr)
print(f'Второй массив с четными элементами:', even)
print(f'Выделенная память: {getsizeof(arr) + getsizeof(i)}')

#3.8
from sys import getsizeof

matrix = [[] for _ in range(4)]

for line in matrix:
    line_sum = 0
    for i in range(4):
        num = int(input('Введите число: '))
        line.append(num)
        line_sum += num
    line.append(line_sum)
    
for line in matrix:
    for num in line:
        print(f'\t{num:5}', end = ' ' )
    print()
print(f'Выделенная память: {getsizeof(line) + getsizeof(num) + getsizeof(line_sum) + getsizeof(i)}')   
