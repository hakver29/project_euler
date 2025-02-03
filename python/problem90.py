from itertools import combinations, permutations


def get_squares():
    return [i**2 for i in range(1, 10)]

def get_dices():
    digits = [0,1,2,3,4,5,6,7,8,9]
    perm = list(set(combinations(digits, 6)))
    perm = [sorted(p) for p in perm]
    return perm

def check_cases(i,j, squares):
    L = []
    if int(str(i) + str(j)) in squares:
        L.append(int(str(i) + str(j)))
    if int(str(j) + str(i)) in squares:
        L.append(int(str(j) + str(i)))

    if i == 6:
        if int(str(j) + str(9)) in squares:
            L.append(int(str(j) + str(9)))
    if j == 6:
        if int(str(i) + str(9)) in squares:
            L.append(int(str(i) + str(9)))

    if i == 9:
        if int(str(6) + str(j)) in squares:
            L.append(int(str(6) + str(j)))
    if i == 9:
        if int(str(j) + str(6)) in squares:
            L.append(int(str(j) + str(6)))
    if j == 9:
        if int(str(i) + str(6)) in squares:
            L.append(int(str(i) + str(6)))
    if j == 9:
        if int(str(6) + str(i)) in squares:
            L.append(int(str(6) + str(i)))
    return L

def check_dices(dice1, dice2, squares):
    L = []
    for i in dice1:
        for j in dice2:
            L = L + check_cases(i,j,squares)


    L = list(set(L))
    L.sort()

    if L == squares:
        return True
    return False

def main():
    squares = get_squares()
    dices = get_dices()
    S = 0
    N = []
    dice_combinations = list(permutations(dices, 2))
    for (dice1, dice2) in dice_combinations:
        if check_dices(dice1, dice2, squares):
            M = sorted([dice1, dice2])
            if M not in N:
                N.append(M)
                S += 1
    return S

print(main())