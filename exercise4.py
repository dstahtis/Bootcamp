import math
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
i = b**2 - 4 * a * c
if i < 0:
    print("No real-valued solutions exist")
else:
    x_plus = (-b + i) / 2 * a
    x_minus = (-b - i) / 2 * a
    print("X(+): ", x_plus)
    print("X(-): ", x_minus)
    
