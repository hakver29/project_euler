
def remainder(a, n):
    if n % 2 == 0:
        return 2
    return (2*n*a ) % (a*a)

def main():
    LIMIT = 1000
    S = 0
    for a in range(3, LIMIT + 1):
        L = []
        n = 1
        temp_r = remainder(a, n)
        while temp_r not in L:
            L.append(temp_r)
            n += 2
            temp_r = remainder(a, n)
            # print(a,n,temp_r)
        S += max(L)
    return S


if __name__ == '__main__':
    print(main())