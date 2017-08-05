import math


class MyRange:
    def __init__(self, first, second=None, step=1):
        self.step = step
        if second is None:
            self.start = 0
            self.end = first
        else:
            self.start = first
            self.end = second

        self.length = math.ceil((self.end - self.start) / self.step)

    def __repr__(self):
        return 'MyRange({},{},{})'.format(self.start, self.end, self.step)

    def __len__(self):
        return self.length

    def __iter__(self):
        for _ in range(len(self)):
            yield self.start
            self.start += self.step

    def __getitem__(self, index):
        if 0 <= index <= len(self):
            return index * self.step + self.start
        else:
            return IndexError


# class RangeIterator:
#     def __init__(self, range_instance):
#         self.range = range_instance
#         self.next_value = self.range.start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         result = self.next_value
#         if self.next_value < self.range.end and self.range.step > 0 or \
#            self.next_value >= self.range.end and self.range.step < 0:
#             self.next_value += self.range.step
#         else:
#             raise StopIteration
#         return result

r = MyRange(11, 4, -1)
print(len(r))
it = iter(r)
for i in it:
    print(i)

print()

r = MyRange(4, 11, 2)
it = iter(r)
for i in it:
    print(i)







