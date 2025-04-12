import sys

def fibonacci(n):
    if n <= 0:
        print("Error!The number you entered is invalid.")
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = fibonacci(n - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

start = int(sys.argv[1])
end = int(sys.argv[2])

fib_sequence = fibonacci(end)
result = []
for i in range(start - 1, end):
    result.append(fib_sequence[i])
print(result)

