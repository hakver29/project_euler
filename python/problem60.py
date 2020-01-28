from itertools import permutations
from sympy import sieve



def check_candidate(candidate:list, primes: list):
    p = list(permutations(candidate,2))
    for i in p:
        x = int(str(i[0]) + str(i[1]))
        y = int(str(i[1]) + str(i[0]))
        if not binary_search(primes, x):
            return False
        if not binary_search(primes,y):
            return False

    return True

def binary_search(item_list,item):
    first = 0
    last = len(item_list)-1
    found = False
    while( first<=last and not found):
        mid = (first + last)//2
        if item_list[mid] == item :
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

def generate_candidates(candidates: list = [], maxPrime: int=10, prime_list: list=[]):
    list_max = maxPrime**2 - 1
    prime_list = [p for p in sieve.primerange(2,list_max)]

    if len(candidates) == 0:
        primes = [[p] for p in sieve.primerange(2,maxPrime)]
        return primes
    else:
        new_candidates = []
        primes = [p for p in sieve.primerange(2, maxPrime)]
        for i in candidates:
            #print(i)
            for j in primes:
                x = i + [j]
                if check_candidate(x, prime_list) == True:
                    new_candidates.append(x)
            #print(i)
        new_candidates = list(set(map(lambda x: tuple(sorted(x)), new_candidates)))
        new_candidates = [list(x) for x in new_candidates]
        return new_candidates


def main():
    max_prime = 10000
    list_max = max_prime ** 2 - 1
    prime_list = [p for p in sieve.primerange(2,list_max)]
    x = generate_candidates(maxPrime=max_prime)
    print(len(x))
    for i in range(4):
        x = generate_candidates(candidates=x, maxPrime=max_prime, prime_list=prime_list)
        print(len(x))

    print(x)
    print(sum(x[0]))

main()