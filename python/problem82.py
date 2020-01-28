def find_sum(i,j,D,matrix):
    X = float('inf')
    for y in range(len(D)):
        Y = 0
        if y > j:
            for m in range(j,y+1):
                Y += matrix[m][i]
            Y += D[y][i-1]
        elif y == j:
            Y = D[y][i-1] + matrix[j][i]
        elif y < j:
            for m in range(y,j+1):
                Y += matrix[m][i]
            Y += D[y][i-1]
        if Y < X:
            X = Y
    return X

def main():
    file = open("p082_matrix.txt", "r")
    M = file.read().split("\n")
    M.pop()
    matrix = []
    for i in M:
        X = [int(j) for j in i.split(",")]
        matrix.append(X)
    size = 80 # Assume matrix is quadratic
    D = [[0 for i in range(size)] for j in range(size)]

    Y = [i for i in range(size)]
    X = [i for i in range(size)]

    #matrix = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]

    for i in range(size):
        for j in range(size):
            if i == 0:
                D[j][0] = matrix[j][0]
            else:
                D[j][i] = find_sum(i,j,D,matrix)

    M = float('inf')
    for i in range(size):
        if D[i][size-1] < M:
            M = D[i][size-1]
    return M
