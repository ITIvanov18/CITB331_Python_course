text = input('Enter some text: ')
histogram = {}

for char in text:
    if char in histogram:
        histogram[char] += 1
    else:
        histogram[char] = 1

print(histogram)

for char, freq in sorted(histogram.items()):
    print(f"{char}: {'*' * freq}")
