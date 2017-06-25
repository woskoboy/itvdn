class Singleton:
    """ Singleton гарантирует, что данный класс имеет только 1 экземпляр """
    _instance = None

    # @classmethod - не требуется, python и так знает об этом спец.методе
    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self.value = "some value"

obj1 = Singleton()
obj2 = Singleton()
# obj1 is obj2 --> True
