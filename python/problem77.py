from sympy import sieve, isprime

def split_number(a):
    m = []

    primes = [p for p in sieve.primerange(2, a)]
    for i in primes:
        if isprime(a-i):
            x = [i,a-i]
            x = sorted(x)
            if x not in m:
                m.append([i,a-i])
    if len(m) == 0:
        return -1
    return m

def split_append(updated_split, split, number):
    temp_split = split_number(number)
    if temp_split != -1:
        append_split = split.copy()
        append_split.remove(number)
        for split2 in temp_split:
            append_split.append(split2[0])
            append_split.append(split2[1])
            append_split.sort()
            #print(append_split)
            if append_split not in updated_split:
                updated_split = updated_split + [append_split]
    return updated_split

def reduce(current_split):
    #print(split_number(10))
    #current_split = split_number(10)
    updated_split = current_split.copy()

    for split in current_split:
        for number in split:
            updated_split = split_append(updated_split, split, number)
            """
            temp_split = split_number(number)
            if temp_split != -1:
                append_split = split
                append_split.remove(number)
                append_split = list(filter(lambda x: x != number, append_split))
                print(append_split)
                for split2 in temp_split:
                    append_split.append(split2[0])
                    append_split.append(split2[1])
                    append_split.sort()
                    print(append_split)
                    if append_split not in updated_split:
                        updated_split = updated_split + [append_split]
            """

    return updated_split

def main():
    current_split = split_number(1000)
    temp_len = -1
    while temp_len != len(current_split)
    updated_split = reduce(current_split)
    updated_split = reduce(updated_split)
    updated_split = reduce(updated_split)
    print(updated_split)

main()






