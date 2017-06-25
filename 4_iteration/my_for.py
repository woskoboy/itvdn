def my_for(iterable, callback):
    it = iter(iterable)
    while True:
        try:
            val = next(it)
            callback(val)
        except StopIteration:
            break


def loop_body(value):
    print('Next value is ', value)

my_for(range(10), loop_body)
