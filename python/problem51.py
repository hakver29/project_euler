import math
import itertools

def isPrime(n):
    for i in range(2,int(math.floor(math.sqrt(n))+1)):
        if n % i == 0:
            return 0
    return 1

def indices(length):
    string = ""
    for i in range(0,length):
        string = string + str(i)
    return list(string)

def replace(number, indices, digit):
    number = list(str(number))
    for i in indices:
        number[int(i)] = str(digit)
    number = "".join(number)
    number = int(number)
    return number

def generate_permutations(length):
    L = ["0"*length]
    start = pow(10,length-1)
    stop = pow(10,length)
    for i in range(start,stop):
        L.append(str(i))
    return L

# k: number of free variables in number
# length: length of number
def solve_one_instance(length, k):
    ind = indices(length)
    num_permutations = generate_permutations(k)
    ind_permutations = [''.join(x) for x in itertools.combinations(ind,length-k)]
    print(num_permutations)
    print(ind_permutations)
    print(ind)


# perm_index: the indices that will be iterated
# rest_number: rest of the number
# length: length of the total number
# returns the generalized number on list form
def get_instance(length, perm_index, rest_number):
    number = []
    for i in range(length):
        if str(i) in perm_index:
            number.append("*")
        else:
            number.append(rest_number[0])
            rest_number = rest_number[1:]
    return number

def solve_instance(length, perm_index, rest_number):
    num_prime = 0
    for i in range(0,10):
        number = get_instance(length, perm_index, rest_number)
        T = number
        for j in range(len(T)):
            if T[j] == "*":
                T[j] = str(i)
        T = int("".join(T))
        if not len(str(T)) < length:
            num_prime += isPrime(T)
    return num_prime

def get_lowest_prime_in_instance(length,perm_index,rest_number):
    for i in range(0,10):
        number = get_instance(length, perm_index, rest_number)
        T = number
        for j in range(len(T)):
            if T[j] == "*":
                T[j] = str(i)
        T = int("".join(T))
        if not len(str(T)) < length:
            if isPrime(T):
                return T
    
def solve_length(length):
    ind = indices(length)
    temp = 0
    for perm_num in range(1,length):
        perm_ind = [''.join(x) for x in itertools.combinations(ind,perm_num)]
        rest_num = generate_permutations(length-perm_num)
        for i in perm_ind:
            for j in rest_num:
                X = solve_instance(length,i, j)
                if X == 8:
                    return get_lowest_prime_in_instance(length,i,j)
        
def main():
    length = 6
    return solve_length(6)
    
    
        
    
        

    
    
