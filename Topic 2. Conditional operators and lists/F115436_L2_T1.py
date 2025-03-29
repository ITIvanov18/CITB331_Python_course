import sys

# Вземане на аргументите от командния ред
list_brat = sys.argv[1:]

is_sorted = True
for i in range(len(list_brat) - 1):
    if list_brat[i] > list_brat[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("sorted")
else:
    print("unsorted")
