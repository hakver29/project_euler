L = 12000
minK = [float('inf') for i in range(0, L)]

def valid(n, k):
    if k >= len(minK):
        return False
    if minK[k] > n:
        minK[k] = n
        return True
    return False

def getMinK(n, p, s, depth = 1, minFactor = 2):
    if p == 1:
        if valid(n, depth + s - 1):
            return 1
        else:
            return 0

    result = 0
    if depth > 1:
        if p == s:
            if valid(n, depth):
                return 1
            else:
                return 0
        if valid(n, depth + s - p):
            result += 1

    i = minFactor
    while i*i <= p:
        if p % i == 0:
            result += getMinK(n, p // i, s - i, depth + 1 , i)
        i += 1

    return result

def main():
    s = 0
    n = 4
    todo = L - 2
    while todo > 0:
        f = getMinK(n,n,n)
        if f > 0:
            todo -= f
            s += n
        n += 1

    return s

print(main())