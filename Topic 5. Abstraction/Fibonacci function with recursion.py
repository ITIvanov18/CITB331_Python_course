def fibonacci(n):
    if n <= 0:
        print("Error")
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    num_list = fibonacci(n - 1)
    num_list.append(num_list[-1] + num_list[-2])
    return num_list


print(fibonacci(20))