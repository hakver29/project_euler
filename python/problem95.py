import math

def sum_div(num):
    result = 0

    i = 2
    while i <= (math.sqrt(num)):
        if (num % i == 0):
            if (i == (num / i)):
                result = result + i;
            else:
                result = result + (i + num / i);
        i = i + 1

    return (result + 1);

def get_chain_length(number):
    chain = [number]
    max_size = 1000000
    i = 0
    next_element = sum_div(number)

    while next_element not in chain and next_element < max_size and len(chain) < 50:
        chain.append(next_element)
        next_element = sum_div(next_element)
        i += 1

    if next_element == number:
        return [len(chain), min(chain)]
    return [0,max_size]

def main():
    n_max = 0
    min_element = 0
    for i in range(100,1000000):
        [chain_length, temp_min_element] = get_chain_length(i)
        if chain_length > n_max:
            n_max = chain_length
            min_element = temp_min_element
            print(n_max, min_element)

        if i % 100000 == 0:
            print(i)

    print(n_max, min_element)

main()

print(sum_div(220))
#print(sum_div(284))
#print(get_chain_length(12496))