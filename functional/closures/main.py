import math


def add_1(x):
    return x + 1


def fun(f, x):
    return f(f(x))

print fun(add_1, 5)

# Distance between two points:

a = (5, 0)
b = (5, 5)


def distance(a, b):
    x = math.fabs(a[0] - b[0])
    y = math.fabs(a[1] - b[1])
    return math.sqrt(x * x + y * y)

print distance(a, b)
