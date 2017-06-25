class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return "Rectangle(%.1f, %.1f)" % (self.a, self.b)


class Circle:
    def __init__(self, r):
        self.r = r

    def __repr__(self):
        return "Circle(%.1f)" % self.r

    @classmethod
    def from_rec(cls, rec):
        r = (rec.a ** 2 + rec.b ** 2) ** 0.5 / 2
        return cls(r)

rec = Rectangle(3, 4)
print(rec)
cir = Circle(1)
print(cir)
cir2 = Circle.from_rec(rec)
print(cir2)

