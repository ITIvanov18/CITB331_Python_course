def fibonacci():
    a = 0
    b = 1
    tmp = 0
    yield a
    yield b
    while 1:
        tmp = a + b
        yield tmp
        a = b
        b = tmp

for i in fibonacci():
    print(i)
    if i > 100:
        break

fib = fibonacci()
print(next(fib))
print(next(fib))
print(next(fib))
