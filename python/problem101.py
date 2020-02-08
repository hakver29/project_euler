import math

def eval(n):
    s = 1 - n + pow(n,2) - pow(n,3) + pow(n,4) - pow(n,5) + pow(n,6) - pow(n,7) + pow(n,8) - pow(n,9) + pow(n,10)
    return s


def check_polynomial(degree):
    L = [0]*(degree+1)

print(eval(1))
print(eval(2))
print(eval(3))