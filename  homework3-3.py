# Задание №3. В массиве случайных целых чисел поменять местами минимальный и максимальный
# элементы.

from random import random
length = 15
arr = [0] * length
for i in range (length):
    arr[i] = int(random() * 100)
    print(arr[i], end = ' ')
print()

min_number = min(arr)
max_number = max(arr)
imin_number = arr.index(min_number)
imax_number = arr.index(max_number)
print('arr[%d] = %d arr arr[%d] = %d' % (imin_number + 1, min_number, imax_number +1, max_number))
arr[imin_number], arr[imax_number] = arr[imax_number], arr[imin_number]

#mn = 0
#mx = 0
#for i in range(length):
#   if arr[i] < arr[mn]:
#        mn = i
#    elif arr[i] > arr[mx]:
#        mx = i
#    print('arr[%d] = %d arr[%d] = %d' % (mn + 1, arr[mn], mx + 1, arr[mx]))
#    b =arr[mn]
#    arr[mn] = arr[mx]
#    arr[mx] = b
#for i in range(15):
#    print(arr[i], end = ' ' )
#print()