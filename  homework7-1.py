# Задание №1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и
# отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

import random

arr = [random.randint(-100, 99) for _ in range(15)]

def sort_arr(numb_arr):
    for k in range(len(numb_arr) -1):
        for i in range(len(numb_arr) -1 - k):
            if numb_arr[i] < numb_arr[i+1]:
                numb_arr[i], numb_arr[i+1] = numb_arr[i+1], numb_arr[i]
    return numb_arr

print(f'Исходный массив:',  arr)
print(f'Отсортированный массив:', sort_arr(arr))