import math
from bisect import bisect_left


def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1

def SieveOfEratosthenes(num):
    P = []
    prime = [True for i in range(num + 1)]
    # boolean array
    p = 2
    while (p * p <= num):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):

            # Updating all multiples of p
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, num + 1):
        if prime[p]:
            P.append(p)
    return P

def is_cube(n):
    cube_root = n**(1./3.)
    if round(cube_root) ** 3 == n:
        return True
    else:
        return False

def get_cube(n):
    return round(n**(1./3.))

def main():
    M = 1000000
    S = 0
    P = SieveOfEratosthenes(M)
    cubes = [i**3 for i in range(1,M*1000)]

    for n in cubes:
        n_cube_root = get_cube(n)
        for m in range(n,M*1000, n_cube_root):
            N = (m**3 - n**3)/(n**2)
            X = BinarySearch(P, N)
            if X != -1:
                print(n,m, X, N)
                #print(m**3 == n**3 + n**2 * X)
                S += 1
                break

    return S

print(main())