# Задание №2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение -
# [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

message = 'Введите 2 числа с использованием следующих символов: от 0 до 9 и от A до F '
# 
array = input(message).upper().split()
# mult = 0
# for a in range():
#     a = []
#     if a in range([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F]):
#         print(a)
#     else:
#         print('Ввели неправильные данные')
#         a = list(map(int, input(message).split()))     
# print(a)

import string as st

s = st.digits + st.ascii_uppercase[:6]
d = {char: index for index, char in enumerate(s)}
number = array[0][::-1]
number2 = array[1][::-1]

print(d)
# 
# for char in number:
#     print(char)
#     summa += d[char] * 16 ** number.index(char)
# print(summa)

def decimal(num):
    summa = 0
    for char in num:
        summa += d[char] * 16 ** num.index(char)
    return summa

print(decimal(number))
print(decimal(number2))

res1 = decimal(number)
res2 = decimal(number2)

def heximal(n):
    division = 0
    l = []
#     n = []
    while n > 0:
        leftover = n % 16
        for k in d:
            if d[k] == leftover:
                l.append(k)
        n = n //16
    l.reverse()
    return ''.join(l)
                
summa = res1+res2
print(summa)
mult = res1* res2
print(mult)

print(heximal(summa))
print(heximal(mult))


