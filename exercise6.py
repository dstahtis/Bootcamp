i = int(input("Enter number of triangle numbers: "))
for n in range(1, i+1):
    a = int(n * (n + 1) / 2)
    print(a, end = ' ')
