# Квадрат (3)
# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.

# 1
def square(side: int):
    return 4 * side, side * side, side * 2 ** 0.5


sq = square(4)
print(sq)


# 2
class Square:
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return self.side * self.side

    def sq_area(self):
        return self.side * self.side

    def diagonal(self):
        return self.side * 2 ** 0.5


s = Square(int(input('Enter the side of square: ')))

print((s.perimeter(), s.sq_area(), s.diagonal()))
