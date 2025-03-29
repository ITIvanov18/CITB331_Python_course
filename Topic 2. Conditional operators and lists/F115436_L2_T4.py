import sys

spisuk = list(sys.argv[1:])
result = []

for num in spisuk:
    if num not in result:
        result.append(num)

result.sort()

print(result)