# This is a sample Python script.

import sys

# Прочитане на коефициентите от командния ред
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a == 0:
    print("special case")
else:
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        print("no real roots")
    elif discriminant == 0:
        x = (-b) / (2 * a)
        print(f"{x:g}")
    else:
        sqrt_d = discriminant**0.5
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        print(f"{x1:g}|{x2:g}")