
def main():
    file = open("p081_matrix.txt", "r")
    M = file.read().split("\n")
    M.pop()
    matrix = []
    for i in M:
        X = [int(j) for j in i.split(",")]
        matrix.append(X)
    size = len(X) # Assume matrix is quadratic
    D = [[0 for i in range(size)] for j in range(size)]

    for i in range(size):
        for j in range(size):
            if i == 0 and j == 0:
                D[i][j] = matrix[i][j]
            elif i == 0 and j != 0:
                D[i][j] = D[i][j-1] + matrix[i][j]
            elif j == 0 and i != 0:
                D[i][j] = D[i-1][j] + matrix[i][j]
            else:
                D[i][j] = min(D[i-1][j] + matrix[i][j], D[i][j-1] + matrix[i][j])
    return D[size-1][size-1]
