import math
from math import isqrt

N = 1000000000

def is_square(i):
    return i == isqrt(i) ** 2

def Heron(i):
    S = 0

    if is_square((3*i*i - 2*i - 1)//4) == True and 3 * i + 1 <= N:
        S += 3 * i + 1

    if is_square((3*i*i + 2*i - 1)//4) == True and 3 * i - 1 <= N:
        S += 3 * i - 1

    return S

def main():
    S = 0
    for i in range(3, int(N/3), 2):
        A = Heron(i)
        if A != 0:
            S += A

    return S

print(main())