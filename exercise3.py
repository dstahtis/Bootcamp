import math
print("What's the size of each side of your triangle?")
alpha = int(input("a: "))
beta = int(input("b: "))
gamma =int(input("c: "))
area = 0.25 * math.sqrt((alpha + beta + gamma) * (-alpha + beta + gamma) * (alpha - beta + gamma) * (alpha + beta + gamma))
print("Total area of your triangle = ", area)
