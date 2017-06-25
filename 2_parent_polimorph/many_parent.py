# class Base:
#     def method(self):
#         """ __name__ - имя класса экземпляра """
#         print('Base method invoked on ', type(self).__name__, 'instance')
#
#
# class Child(Base):
#     """ проблемы без использования super:
#     - нужно точно знать имя базового класса (если поменяется иерархия наследования,
#                                  нам нужно будет поменять имя баз.класса вручную)
#     - проблемы при множественном наследовании """
#     def method(self):
#         # Base.method(self)
#         # super(Child, self).method()
#         # super(__class__, self).method()
#         super().method()  # базовый класс становится известным при выполнении super()
#         print('Child method invoked on ', type(self).__name__, 'instance')

# class A:
#     def method(self):
#         print("A method!")
#
#
# class B(A):
#     pass
#
#
# class C(A):
#     def method(self):
#         print("C method")
#
#
# class D(B, C):
#     pass
#
# obj = D()
# obj.method()


class Animal:
    def __init__(self):
        self.can_run = False
        self.can_fly = False

    def print_abilities(self):
        print(type(self).__name__)
        print('Can run:', self.can_run)
        print('Can fly:', self.can_fly)
        print()


class Horse(Animal):
    def __init__(self):
        """ super(__class__, self):
        super ищет в MRO объекта self след-й класс после текущего __class__
        pegas.__class__.__mro__ ==> Pegasus, Horse, Bird, Animal, object;
        а значит после текущего Horse следующий ==> Bird
        обращаемся к атрибутам найденного класса Bird ==> методу __init__() """
        super().__init__()
        self.can_run = True


class Bird(Animal):
    def __init__(self):
        super().__init__()  # идём в Animal
        self.can_fly = True


class Pegasus(Horse, Bird):
    """ конструктор в Python наследуется как и другие методы,
    __init__ наследуется по MRO от Horse """
    pass


def main():
    h = Horse()
    h.print_abilities()

    b = Bird()
    b.print_abilities()

    pegas = Pegasus()
    print(pegas.__class__.__mro__)
    pegas.print_abilities()

main()
