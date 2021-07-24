# Задание №3. Сформировать из введенного числа обратное по порядку входящих в него
# цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843

number = int(input('Введите число: '))
reversed_number = 0

while number > 0:
    digit = number % 10
    number = number // 10
    reversed_number = reversed_number * 10
    reversed_number = reversed_number +digit
    
print((f'Обратное число ='), reversed_number)