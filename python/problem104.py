def check_fib(a):
    S = '123456789'
    a = str(a)
    first = a[0:9]
    last = a[-9:len(a)]

    first = ''.join(sorted(first))
    last = ''.join(sorted(last))
    if first == S and last == S:
        return True
    else:
        return False

def main():
    i = 3
    n1 = 1
    n2 = 1
    while True:
        n3 = n1 + n2
        if check_fib(n3):
            return i
        i += 1
        n1 = n2
        n2 = n3


print(main())