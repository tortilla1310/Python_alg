# Задание №4. Определить, какое число в массиве встречается чаще всего.

from random import random
length = 15
arr = [0] * length
for i in range(length):
    arr[i] = int(random() * 7)
print(arr)

num = arr[0]
max_frq = 1
for i in range(length-1):
    frq = 1
    for k in range (i+1, length):
        if arr[i] ==arr[k]:
            frq +=1
    if frq > max_frq:
        max_frq = frq
        num = arr[i]
        
if max_frq > 1:
    print('Число', num, 'встречается', max_frq, 'раз(а)')
else:
    print('Все элементы уникальны')
