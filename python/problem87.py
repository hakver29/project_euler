from sympy import sieve
import math

N = 50000000

L = [0]*50000000
quad =[i for i in sieve.primerange(1, math.floor(math.pow(N,1/2)))]
cub = [i for i in sieve.primerange(1, math.floor(math.pow(N,1/3)))]
quar = [i for i in sieve.primerange(1, math.floor(math.pow(N,1/4)))]

for i in quar:
    print(i)
    for j in cub:
        for k in quad:
            x = i**4+j**3+k**2
            if x < N:
                L[x] = 1

print(sum(L))
