class Matrix:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, other):
        if isinstance(other, Matrix):
            return Matrix(
                self.a + other.a, self.b + other.b,
                self.c + other.c, self.d + other.d
            )
        raise ValueError("Can only add another Matrix")

    def __mul__(self, other):
        if isinstance(other, Matrix):
            return Matrix(
                self.a * other.a + self.b * other.c, self.a * other.b + self.b * other.d,
                self.c * other.a + self.d * other.c, self.c * other.b + self.d * other.d
            )
        raise ValueError("Can only multiply by another Matrix")

    def __str__(self):
        return f"[{self.a},{self.b};\n {self.c},{self.d}]"

    def __repr__(self):
        return f"Matrix({self.a}, {self.b}, {self.c}, {self.d})"


if __name__ == '__main__':
    m1 = Matrix(1, 2, 3, 4)
    m2 = Matrix(2, 0, 1, 2)

    m3 = m1 + m2
    print(m3)  # [3,2; 4,6]

    m4 = m1 * m2
    print(m4)  # [4,4; 10,8]

    print(repr(m4))  # Matrix(4,4,10,8)
