# Задание №2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг
# вправо и влево на два знака. Объяснить полученный результат.

bit_or = 5 | 6
bit_xor = 5 ^ 6
bit_and = 5 & 6
bit_right = 5 << 2
bit_left = 6 >> 2

print(f'5 | 6  = {bit_or}\n'
    f' 5 ^ 6 = {bit_xor}\n'
    f' 5 & 6 = {bit_and}\n'
    f' 5 << 2 = {bit_right}\n'
    f' 6 >> 2 = {bit_left}\n')