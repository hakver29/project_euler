import math
from functools import lru_cache

def sieve_non_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not prime

    # Sieve of Eratosthenes
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # Collect non-prime numbers
    non_primes = [i for i in range(n + 1) if not is_prime[i]]
    return non_primes[2:]

def sieve_spf():
    spf = list(range(C_LIMIT + 1))  # Smallest prime factor for each number

    # Using the Sieve of Eratosthenes to fill SPF array
    for i in range(2, int(C_LIMIT**0.5) + 1):
        if spf[i] == i:  # i is a prime
            for j in range(i * i, C_LIMIT + 1, i):
                if spf[j] == j:  # Mark SPF only if it's not marked yet
                    spf[j] = i
    return spf

def get_radicals():
    return [math.prod(get_distinct_prime_factors(i, spf)) for i in range(1, C_LIMIT + 1)]

def get_sorted_radicals():
    rads = [0] + [1] * (C_LIMIT - 1)
    for i in range(2, len(rads)):
        if rads[i] == 1:
            for j in range(i, len(rads), i):
                rads[j] *= i

    sortedrads = sorted((rad, n) for (n, rad) in enumerate(rads))
    sortedrads = sortedrads[1 : ]  # Get rid of the (0, 0) entry
    return sortedrads

def get_distinct_prime_factors(n, spf):
    if n == 1:
        return [1]
    prime_factors = set()
    while n > 1:
        prime_factors.add(spf[n])
        n //= spf[n]
    return sorted(list(prime_factors))

@lru_cache(None)
def prod(factors: tuple):
    return math.prod(factors)

def loop_triples():
    s = 0
    n = 0
    non_primes = sieve_non_primes(C_LIMIT)
    for c_it in non_primes:
        rad_c_it = radicals[c_it-1]
        for (rad, a) in sorted_radicals:
            total_rad = rad
            total_rad *= rad_c_it
            if total_rad >= c_it:
                break
            b = c_it - a
            if a < b and total_rad * radicals[b-1] < c_it and math.gcd(a,b) == 1:
                s += c_it
                n += 1

    return (s,n)


def main():
    global C_LIMIT
    C_LIMIT = 120000
    global spf
    spf = sieve_spf()
    global radicals
    radicals = get_radicals()
    global sorted_radicals
    sorted_radicals = get_sorted_radicals()
    return loop_triples()


if __name__ == '__main__':
    print(main())
