class Figure:
    def __init__(self, side=0):
        self.side = side


class Square(Figure):
    def draw(self):
        for _ in range(self.side):
            print('* ' * self.side)


class Triangle(Figure):
    def draw(self):
        for i in range(1, self.side + 1):
            print('* ' * i)

s = Square(5)
s.draw()
t = Triangle(5)
t.draw()


# class Base:
#     def method(self):
#         print("Hello")
#
#
# class Child(Base):
#     def child_method(self):
#         print("Hello Child")
#
#     def method(self):
#         print("Hello from redefined method!")
#
# c = Child()
# c.method()
# c.child_method()
