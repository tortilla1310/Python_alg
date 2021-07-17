# Задние №5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

letter1 = input('введите одну букву латинского алфавита: ')
letter2 = input('введите вторую букву латинского алфавита: ')

placement1 = ord(letter1) - 96
placement2 = ord(letter2) - 96
distance = abs(placement1 - placement2)-1

print(f'Буква "{letter1}" {placement1}-я в алфавите\n' 
      f'Буква "{letter2}" {placement2}-я в алфавите\n'
      f'Расстояние между буквами: {distance}')