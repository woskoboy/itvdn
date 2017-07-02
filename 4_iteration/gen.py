def fibo(count):
    first, second = 0, 1
    for _ in range(count):
        yield second
        result = first + second
        first, second = second, result
        # yield second
        # first, second = second, first + second

count = int(input('How many Fibonacci numbers? '))
for val in fibo(count):
    print(val)



