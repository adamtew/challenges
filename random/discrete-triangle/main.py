def triangle(n):
    if n == 1:
        return 3
    elif n == 0:
        return 1
    else:
        return 2 * triangle(n - 1) + triangle(n - 2)

for i in range(0, 10):
    print i, triangle(i)
