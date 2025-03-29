import sys

list_brat = list(sys.argv[1:])
duplicate = False

for i in range(len(list_brat)):
    for j in range(i+1, len(list_brat)):
        if list_brat[i] == list_brat[j]:
            duplicate = True
            break
    if duplicate:
        break

print(duplicate)

