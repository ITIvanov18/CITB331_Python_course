# Да се реализира алгоритъма за шифриране на Цезар

import sys
import string

text = sys.argv[1]
key = int(sys.argv[2])

uppercase = string.ascii_uppercase    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
lowercase = string.ascii_lowercase    # abcdefghijklmnopqrstuvwxyz

result = ""
for char in text:
    if char in uppercase:
        index = (uppercase.index(char) + key) % 26
        result += uppercase[index]
    elif char in lowercase:
        index = (lowercase.index(char) + key) % 26
        result += lowercase[index]
    else:
        result += char

print(result)

