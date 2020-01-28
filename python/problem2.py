def main():
    S = 2
    L = [1,2]
    while L[-1] < 4000000:
        L.append(L[-1]+L[-2])
        if L[-1] % 2 == 0:
            S += L[-1]
    return S

print(main())
