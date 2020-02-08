import math

def is_integer(n):
    a = math.sqrt((2*n*n-2*n+1)/4) + (1/2)
    if a == int(a):
        return a
    else:
        return -1

def main():
    n = 1000000000000

    while is_integer(n) == -1:
        print(n)
        n += 1
    print(is_integer(n))

main()
