from itertools import product
import math

def get_permutations(digits, number_length, remove_zeros=False):
    if remove_zeros:
        return [perm for perm in product([0, 1, 2, 3], repeat=digits) if sum(perm) == number_length - 1 and perm[0] < 3]

    return [perm for perm in product([0, 1, 2, 3], repeat=digits) if sum(perm) == number_length]

def get_number_combinations(perm):
    S = 1
    permsum = sum(perm)
    for i in perm:
        S *= math.comb(permsum, i)
        permsum -= i
    return S


def main():
    permutations_leading_zero = get_permutations(10, 18, True)
    permutations = get_permutations(10, 18, False)

    S = 0
    for i in permutations:
        S += get_number_combinations(i)


    for j in permutations_leading_zero:
        S -= get_number_combinations(j)

    return S

print(main())