

n1 = [int(n*(n+1)/2) for n in range(1,200) if n*(n+1)/2 < 10000 and n*(n+1)/2 > 1000]
n2 = [int(n*n) for n in range(1,200) if n*n < 10000 and n*n > 1000]
n3 = [int(n*(3*n-1)/2) for n in range(1,200) if n*(3*n-1)/2 < 10000 and n*(3*n-1)/2 > 1000]
n4 = [int(n*(2*n-1)) for n in range(1,200) if n*(2*n-1) < 10000 and n*(2*n-1) > 1000]
n5 = [int(n*(5*n-3)/2) for n in range(1,200) if n*(5*n-3)/2 < 10000 and n*(5*n-3)/2 > 1000]
n6 = [int(n*(3*n+2)) for n in range(1,200) if n*(3*n+2) < 10000 and n*(3*n+2) > 1000]


print(len(n1))
print(len(n2))
print(len(n3))
print(len(n4))
print(len(n5))
print(len(n6))