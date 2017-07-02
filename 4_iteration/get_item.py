class SimpleIterable:
    def __getitem__(self, index):
        if 0 <= index <= 5:
            return index * 2
        else:
            raise IndexError

iterable = SimpleIterable()
for val in iterable:
    print(val)

iterator = iter(iterable)
print(iterator)
