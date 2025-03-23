def get_sorted_radicals():
    rads = [0] + [1] * (C_LIMIT - 1)
    for i in range(2, len(rads)):
        if rads[i] == 1:
            for j in range(i, len(rads), i):
                rads[j] *= i

    sortedrads = sorted((rad, n) for (n, rad) in enumerate(rads))
    sortedrads = sortedrads[1 : ]  # Get rid of the (0, 0) entry
    return sortedrads


def main():
    global C_LIMIT
    C_LIMIT = 100001
    radicals = get_sorted_radicals()
    print(radicals[9999][1])

main()