class MyObject:

    def __init__(self):
        self.__x = 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if val < 100:
            self.__x = val

obj = MyObject()
print(obj.x)
obj.x = 5
print(obj.x)
