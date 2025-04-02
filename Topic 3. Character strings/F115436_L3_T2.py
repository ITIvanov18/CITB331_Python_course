# Да се реализира на python алгоритъм за шифриране на Виженер

import sys

text = sys.argv[1]
key = sys.argv[2]

result = ""
key_length = len(key)
key_index = 0

for char in text:
    if char.isalpha():
        shift = ord(key[key_index % key_length].upper()) - ord('A')
        if char.isupper():
            start = ord('A')
        else:
            start = ord('a')
        result += chr((ord(char) - start + shift) % 26 + start)
        key_index += 1  # Увеличава се само ако е обработена буква
    else:
        result += char

print(result)
