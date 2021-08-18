# Задание №1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в
# рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

import cProfile

def count_numbers(number:str):
    odd  = 0
#     odd = even =  0
    for num in number:
#         if int(num) % 2:
#             odd += 1
#         else:
#             even += 1
        odd += 1 if int(num) % 2 else 0
    return len(number) -odd, odd

def main():
    number = input('Введите натуральное число: ')
    even, odd = count_numbers(number)
    print(f'в {number}: {even} четных чисел и {odd} нечетных чисел')
    
if __name__ == '__main__':
    cProfile.run('main()')
    

   
   
   
# number = input('Введите натуральное число: ')

# odd = 0
# even = 0
# for num in number:
#     if int(num) % 2 ==0:
#         even +=1
#     else:
#         odd +=1
# print(f'в {number}: {even} четных чисел и {odd} нечетных чисел')