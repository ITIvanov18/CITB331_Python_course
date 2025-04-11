def power_func(x, n):
    if n == 0:
        return 1
    else:
        return x * power_func(x, n - 1)

print(power_func(2, 5))