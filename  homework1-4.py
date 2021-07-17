# 4. Написать программу, которая генерирует в указанных пользователем границах:

# - случайное целое число;
# - случайное вещественное число;
# - случайный символ.

# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

# целое число:
import random
integer1 = int(input('введите нижнюю границу целого числа: ' ))
integer2 = int(input('введите верхнюю границу числа: '))

number_int = random.randint(integer1, integer2)
print(f'случайное целое число: {number_int}\n')

# вешественное число:
realNumber_start = float(input('введите нижнюю границу вещественного числа: ' ))
realNumber_end = float(input('введите верхнюю границу числа: ' ))
number_float = random.uniform(realNumber_start, realNumber_end)
print(f'случайное вещественное число: {number_float}\n')

# символ:
symbol_start = input('введите первый символ: ' ).lower()
symbol_end = input('введите последний символ: ').lower()

symbol_char = chr(random.randint(ord(symbol_start), ord(symbol_end)))
print(f'случайный символ:  {symbol_char}\n')
