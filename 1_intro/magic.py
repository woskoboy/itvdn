class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __repr__(self):
        return "Complex({},{})".format(self.real, self.img)

    def __str__(self):
        return "{}{:+d}i".format(self.real, self.img)

    def __add__(self, other):
        return Complex(self.real + other.real, self.img + other.img)

    def __eq__(self, other):
        return self.real == other.real and self.img == other.img

a = Complex(2, 3)
b = Complex(2, 2)
c = Complex(2, 2)
r = a + b
# b is c --> False
# b == c --> True


