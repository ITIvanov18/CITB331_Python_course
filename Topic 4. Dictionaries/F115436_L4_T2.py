import sys

inputText = sys.argv[1]
frequency = {}

for letter in inputText:
    if letter in frequency:
        frequency[letter] += 1
    else:
        frequency[letter] = 1

print(sorted(frequency.items()))
