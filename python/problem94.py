import math

def is_square(integer):
    root = math.sqrt(integer)
    return integer == int(root + 0.5) ** 2

def area(i,up):
    if up == True:
        a1 = (3*i+1)/2
        a4 = (i - 1) / 2
        square = int(a1*a4)
        print(square)
        if is_square(square):
            return True
        else:
            return False
    else:
        a1 = (3*i-1)/2
        a4 = (i - 3) / 2
        square = int(a1*a4)
        print(square)
        if is_square(square):
            return True
        else:
            return False


N = 1000000000
S = 0
upper_limit_area = int(math.ceil(pow(16*(N**2)/3 - 1,1/4)))

for i in range(3,upper_limit_area-1000,2):
    A1 = area(i,True)
    A2 = area(i, False)
    if A1:
        S += 3*i+1
    if A2:
        S += 3*i-1

print(S)