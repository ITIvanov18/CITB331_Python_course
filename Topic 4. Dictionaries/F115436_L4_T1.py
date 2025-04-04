import sys

rechnik = {1: 'a', 2: 'b', 3: 'c', 4: 'a', 5: 'd', 6: 'e', 7: 'a', 8: 'b'}

value = sys.argv[1]
keys_list = []
for k, v in rechnik.items():
    if v == value:
        keys_list.append(k)

print(keys_list)