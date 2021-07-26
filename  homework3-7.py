# Задание №7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут
# быть как равны между собой (оба являться минимальными), так и различаться.

import random

num_list = [random.randint(1, 101) for _ in range(10)]
min_el = num_list[1]
sec_min = num_list[0]

for num in num_list:
    if num <= min_el:
        sec_min = min_el
        min_el = num
    elif num <= sec_min:
        sec_min = num
print(f' В массиве: \n{num_list}\nминимальные элементы {min_el} и {sec_min}')