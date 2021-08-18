# Задание №2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

import math

def without_eratosthenes(i): # без алгоритма "Решето Эратосфена"
    
    list_prime = [2]
    number = 3
    while len(list_prime) < 1:
        flag = True
        for j in list_prime:
            if number % j == 0:
                flag = False
                break
        if flag:
            list_prime.append(number)
        number +=1
    return list_prime[-1]

def prime_counting_function(i):
    number_of_primes = 0
    number = 2
    while number_of_primes < i:
        number_of_primes = number / math.log(number)
        number +=1
    return number

def eratosthenes(i):
    i_max = prime_counting_function(i)
    list_prime = [i for i in range(2, i_max)]
    
    for number in list_prime:
        if list_prime.index(number) <= number -1:
            for j in range(2, len(list_prime)):
                if number * j in list_prime[number:]:
                    list_prime.remove(number * j)
        else:
            break
    return list_prime[i-1]

user_number = int(input('Введите номер по счету простого числа: '))


print('Алгоритм без использования алгоритма «Решето Эратосфена»')
print(f'{without_eratosthenes(user_number)} - {user_number} по счёту простое число')

print('Алгоритм с использованием алгоритма «Решето Эратосфена»')
print(f'{eratosthenes(user_number)} - {user_number} по счёту простое число')
            