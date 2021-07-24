# Задание №9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на
# экран это число и сумму его цифр.

number = int(input('введите числа через "Enter": \nДля остановки ввода чисел нажмите 0 \n'))
max_a = 0
max_b = 0
while number != 0:
    b = number
    a = 0
    while number > 0:
        a += number%10
        number //= 10
    if a > max_a:
        max_a = a
        max_b = b
    number = int(input())
print('Число', {max_b}, 'с максимальной суммой цифр:', {max_a})