"""
Using the recurrence relation described in
http://www.uvm.edu/~mrombach/173_rombach_notes13.pdf
"""

# m = 100 for solution
def main(m):

    p = [[0 for i in range(m+1)] for j in range(m+1)]

    for i in range(1,m+1):
        p[i][1] = 1

    for k in range(2,m+1):
        for n in range(1,m+1):
            if (n-1 < 0 or k-1 < 0) and n-k < 0:
                p[n][k] = 0
            elif n-1 < 0 or k-1 < 0:
                p[n][k] = p[n-k][k]
            elif n-k < 0:
                p[n][k] = p[n-1][k-1]
            else:
                p[n][k] = p[n-1][k-1] + p[n-k][k]

    return sum(p[m])-1
