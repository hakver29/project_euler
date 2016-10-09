import math

def isPrime(n):
    for i in range(2,int(math.floor(math.sqrt(n))+1)):
        if n % i == 0:
            return 0
    return 1


def main():
    S = 0
    for i in range(2,2000000):
        if isPrime(i) == 1:
            S += i
    return S

print(main())
