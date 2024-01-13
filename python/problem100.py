import math
from math import isqrt
def is_square(i):
    return i == isqrt(i) ** 2


def projectEulerProblemOneHundred(n):
    y = 7
    x = 5
    maxY = 2 * n - 1
    while (y <= maxY):
        tempX = 2 * y + 3 * x
        tempY = 3 * y + 4 * x
        y = tempY
        x = tempX
    return (x + 1) / 2

def main():
    n = 1000000000000
    return projectEulerProblemOneHundred(n)

print(main())
#print(is_integer(21))
