import sys

str1 = sys.argv[1]
str2 = sys.argv[2]

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("True")
else:
    print("False")
