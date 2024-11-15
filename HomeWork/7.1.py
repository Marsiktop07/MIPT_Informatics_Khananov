#1/1.1

class vector():
    def __init__(self, x, y, z):
        assert (isinstance(x, float) + isinstance(x, int)) != False, " Координаты должны быть числовыми"
        assert (isinstance(y, float) + isinstance(y, int)) != False, " Координаты должны быть числовыми"
        assert (isinstance(z, float) + isinstance(z, int)) != False, " Координаты должны быть числовыми"
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if type(other) == vector:
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return vector(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other):
        assert other != 0, "Нельзя делить на ноль"
        return vector(self.x / other, self.y / other, self.z / other)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

a = vector(1, 1, 2)
b = vector(2, 3, 4)
print(a + b)
print(b - a)
print(a * b)
print(a * 5)
print(abs(a))


#1.2
k = int(input())
m = []
for i in range(k):
    x, y, z = list(map(float, input().split()))
    m.append(vector(x, y, z))

ans = 0
ans = m[0]
for i in range(1, len(m)):
    ans += m[i]
print(ans / len(m))
