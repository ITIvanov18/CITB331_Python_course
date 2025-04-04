# Напишете програма, която връща списък от всички ключове, които сочат към
# дадена стойност, а ако няма нито една такава стойност, то да се връща празен списък

hashmap = {'k1':1, 'k2':2, 'k3':3, 'k4':1, 'k5':5, 'k6':1}
target = input('What value are you looking for? ')
target = int(target)

keys = []
for key, value in hashmap.items():
    if value == target:
        keys.append(key)

print("The keys which point to that value are", keys)

