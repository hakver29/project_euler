def is_cyclic(x, y):
    if (x % 100) == int(str(y // 100)):
        return True
    return False


def compute():
    tri = [(int(x * (x + 1) / 2), "triangle") for x in range(1, 1000) if 999 < x * (x + 1) / 2 < 10000]
    sq = [(int(x * (x)), "square") for x in range(1, 1000) if 999 < x * (x) < 10000]
    pen = [(int(x * (3 * x - 1) / 2), "pentagonal") for x in range(1, 1000) if 999 < x * (3 * x - 1) / 2 < 10000]
    hexa = [(int(x * (2 * x - 1)), "hexagonal") for x in range(1, 1000) if 999 < (x * (2 * x - 1)) < 10000]
    hep = [(int(x * (5 * x - 3) / 2), "heptagonal") for x in range(1, 1000) if 999 < x * (5 * x - 3) / 2 < 10000]
    octa = [(int(x * (3 * x - 2)), "octagonal") for x in range(1, 1000) if 999 < x * (3 * x - 2) < 10000]

    all_shapes = tri + sq + pen + hexa + hep + octa

    mydict = {}

    for x in all_shapes:
        mydict[x] = []
        for y in all_shapes:
            if x[0] != y[0] and x[1] != y[1]:
                if is_cyclic(x[0], y[0]):
                    mydict[x].append(y)
    print(mydict)
    for a in octa:
        for b in mydict[a]:
            for c in mydict[b]:
                for d in mydict[c]:
                    for e in mydict[d]:
                        for f in mydict[e]:
                            if is_cyclic(f[0], a[0]):
                                print([a[0], b[0], c[0], d[0], e[0], f[0]])
                                if len(set([a[1], b[1], c[1], d[1], e[1], f[1]])) == 6:
                                    print([a[0], b[0], c[0], d[0], e[0], f[0]])
                                    return (sum([a[0], b[0], c[0], d[0], e[0], f[0]]))

print(compute())