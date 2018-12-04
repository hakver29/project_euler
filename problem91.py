import math

def length(a,b):
    return pow(a[0]-b[0],2) + pow(a[1]-b[1],2)

def is_right_triangle(a,b,c):
    L1 = length(a,b)
    L2 = length(b,c)
    L3 = length(a,c)
    M = max(L1,L2,L3)
    if M == L3 and math.fabs(L1 + L2 - L3) < 0.001:
        return 1
    elif M == L2 and math.fabs(L1 + L3 - L2) < 0.001:
        return 1
    elif M == L1 and math.fabs(L2 + L3 - L1) < 0.001:
        return 1
    else:
        return 0
    

def main(n):
    N = 0
    points = []
    for i in range(0,n+1):
        for j in range(0,n+1):
            points.append([i,j])
    del points[0]
    
    x = [0,0]
    for i in range(0,len(points)-1):
        for j in range(i+1,len(points)):
            if is_right_triangle(x,points[i],points[j]):
                N += is_right_triangle(x,points[i],points[j])
    return N
