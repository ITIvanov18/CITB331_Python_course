import sys

def power_func(x, n):
    if n == 0:
        return 1
    else:
        return x * power_func(x, n - 1)

number = int(sys.argv[1])
power = int(sys.argv[2])
print(power_func(number, power))