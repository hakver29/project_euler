from decimal import *
from math import sqrt, isqrt

def is_square(i):
    return i == isqrt(i) ** 2
def getSum(n):
    N = 0
    getcontext().prec = 110  # Change the precision
    n = str(Decimal(n).sqrt()).replace(".", "")
    for i in range(0,100):
        N += int(n[i])
    return N

def main():
    S = 0
    for i in range(1, 100):
        if is_square(i) == False:
            S = S + getSum(i)
    return S

print(main())
