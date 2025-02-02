from itertools import permutations
import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

def get_permutations(nums):
    return list(permutations(nums))

def get_operators():
    operators = "+++---***///"
    return list(set(permutations(operators, 3)))

def get_digits():
    digits = [0,1,2,3,4,5,6,7,8,9]
    digits = list(set(permutations(digits, 4)))
    digits_list = []
    for i in digits:
        d = list(i)
        d.sort()
        if d not in digits_list:
            digits_list.append(d)

    digits_list.sort()
    return digits_list

def get_combinations(a,b,c,d,op1,op2,op3):
    C = []

    try:
        result_1 = ops[op1](a,ops[op2](b,ops[op3](c,d)))
        if (result_1 > 0 and result_1 == int(result_1) and result_1 not in C):
            C.append(int(result_1))
    except ZeroDivisionError:
        pass

    try:
        result_2 = ops[op2](ops[op1](a,b),ops[op3](c,d))
        if (result_2 > 0 and result_2 == int(result_2) and result_2 not in C):
            C.append(int(result_2))
    except ZeroDivisionError:
        pass

    try:
        result_3 = ops[op1](a,ops[op3](ops[op2](b,c),d))
        if (result_3 > 0 and result_3 == int(result_3) and result_3 not in C):
            C.append(int(result_3))
    except ZeroDivisionError:
        pass

    try:
        result_4 = ops[op3](ops[op1](a, ops[op2](b, c)), d)
        if (result_4 > 0 and result_4 == int(result_4) and result_4 not in C):
            C.append(int(result_4))
    except ZeroDivisionError:
        pass

    try:
        result_5 = ops[op3](ops[op2](ops[op1](a, b), c), d)
        if (result_5 > 0 and result_5 == int(result_5) and result_5 not in C):
            C.append(int(result_5))
    except ZeroDivisionError:
        pass

    try:
        result_6 = ops[op3](ops[op2](ops[op1](a, b), c), d)
        if (result_6 > 0 and result_6 == int(result_6) and result_6 not in C):
            C.append(int(result_6))
    except ZeroDivisionError:
        pass

    try:
        result_7 = ops[op1](a, ops[op2](b, ops[op3](c, d)))
        if (result_7 > 0 and result_7 == int(result_7) and result_7 not in C):
            C.append(int(result_7))
    except ZeroDivisionError:
        pass

    return C

def get_all_combinations(a,b,c,d):
    B = []
    perm = list(permutations([a,b,c,d]))
    operators = get_operators()
    for p in perm:
        for o in operators:
            comb = get_combinations(p[0],p[1],p[2],p[3],o[0],o[1],o[2])
            if comb != None:
                B = B + comb
    B.sort()
    B = list(set(B))

    for i in range(1, len(B)):
        if B[i] != B[i-1] + 1:
            return B[:i]
    return B



def main():
    current = 0
    current_digits = [0,0,0,0]
    digits = get_digits()

    for i in digits:
        A = get_all_combinations(i[0],i[1],i[2],i[3])
        if len(A) > current:
            current = len(A)
            current_digits = [i[0], i[1], i[2], i[3]]

    return int(''.join(map(str, current_digits)))


print(main())
