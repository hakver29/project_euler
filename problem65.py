from fractions import gcd


# reducing a fraction on the form 1/(a + (c/b))
def reduce_fraction(a,b,c):
    return b, a*b + c

def gen_list(n):
    L = [2]
    M = 1
    for i in range(n):
        if i % 3 == 1:
            L.append(M*2)
            M += 1
        else:
            L.append(1)
    return L

def sum_digits(X):
    X = list(str(X))
    X = [int(i) for i in X]
    return sum(X)
    

def main(n):
    n -= 1
    L = gen_list(n)
    for i in range(len(L)-2,0,-1):
        if i == len(L)-2:
            a = L[len(L)-2]
            b = L[len(L)-1]
            [x,y] = reduce_fraction(a,b,1)
        else:
            [x,y] = reduce_fraction(L[i],y,x)
    x += y*L[0]
    return sum_digits(x)
