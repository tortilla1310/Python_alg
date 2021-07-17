# Задание №7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков.
#Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

a = float(input('Введите длину отрезка a: '))
b = float(input('Введите длину отрезка b: '))
c = float(input('Введите длину отрезка c: '))

if a + b > c and a + c > b and b + c > a:
    if a == b or b == c or c == a:
        if a == b and a == c:
            print('Треугольник равносторонний')
        else:
            print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Это не треугольник')