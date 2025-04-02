import sys

text = sys.argv[1]
key = int(sys.argv[2])

result = ""
for char in text:
    if char.isupper():
        result += chr((ord(char) + key - 65) % 26 + 65)
    elif char.islower():
        result += chr((ord(char) + key - 97) % 26 + 97)
    else:
        result += char

print(result)