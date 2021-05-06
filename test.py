class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __add__(self, other):
        print(f' Сумма c1 и c2 равна ')
        return f' c = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f' Произведение чисел ')
        return f' c = {self.a * self.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f' c = {self.a} + {self.b} * i'


c_1 = ComplexNumber(26, 3)
c_2 = ComplexNumber(-8, 5)
print(c_1)
print(c_2)
print(c_1 + c_2)
print(c_1 * c_2)