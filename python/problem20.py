def fac(n):
    s = 1
    for i in range(2,n+1):
        s *= i
    return s

def main(n):
    x = list(int(i) for i in list(str(fac(n))))
    return sum(x)

print(main(100))
