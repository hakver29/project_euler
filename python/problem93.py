def checkSum(inner, outer):
    left = outer[0] + inner[0] + inner[1]
    top = outer[1] + inner[1] + inner[2]
    top_right = outer[2] + inner[2] + inner[3]
    bottom_right = outer[3] + inner[3] + inner[4]
    bottom_left = outer[4] + inner[4] + inner[0]
    if bottom_left == left and left == top and top == top_right and top_right == bottom_right and bottom_right == bottom_left:
        return fixFormat(inner, outer)

    return False

def fixFormat(I, O):
    if O[0] < O[1] and O[0] < O[2] and O[0] < O[3] and O[0] < O[4]:
        return [O[0], I[0], I[1],
                O[1], I[1], I[2],
                O[2], I[2], I[3],
                O[3], I[3], I[4],
                O[4], I[4], I[0]]
    if O[1] < O[0] and O[1] < O[2] and O[1] < O[3] and O[1] < O[4]:
        return [O[1], I[1], I[2],
                O[2], I[2], I[3],
                O[3], I[3], I[4],
                O[4], I[4], I[0],
                O[0], I[0], I[1]]
    if O[2] < O[0] and O[2] < O[1] and O[2] < O[3] and O[2] < O[4]:
        return [O[2], I[2], I[3],
                O[3], I[3], I[4],
                O[4], I[4], I[0],
                O[0], I[0], I[1],
                O[1], I[1], I[2]]
    if O[3] < O[0] and O[3] < O[1] and O[3] < O[2] and O[3] < O[4]:
        return [O[3], I[3], I[4],
                O[4], I[4], I[0],
                O[0], I[0], I[1],
                O[1], I[1], I[2],
                O[2], I[2], I[3]]
    if O[4] < O[0] and O[4] < O[1] and O[4] < O[2] and O[4] < O[3]:
        return [O[4], I[4], I[0],
                O[0], I[0], I[1],
                O[1], I[1], I[2],
                O[2], I[2], I[3],
                O[3], I[3], I[4]]

def findMax(L):
    max = 0
    for i in L:
        tempMax = ''
        for j in i:
            tempMax = tempMax + str(j)

        if int(tempMax) > max and len(tempMax) == 16:
            max = int(tempMax)
    return max


def main():
    L = []
    A = [1,2,3,4,5,6,7,8,9,10]
    for a in A:
        B = [x for x in A if x != a]
        for b in B:
            C = [x for x in B if x != b]
            for c in C:
                D = [x for x in C if x != c]
                for d in D:
                    E = [x for x in D if x != d]
                    for e in E:
                        inner = [a,b,c,d,e]


                        F = [x for x in E if x != e]
                        for f in F:
                            G = [x for x in F if x != f]
                            for g in G:
                                H = [x for x in G if x != g]
                                for h in H:
                                    I = [x for x in H if x != h]
                                    for i in I:
                                        J = [x for x in I if x != i]
                                        for j in J:
                                            outer = [f,g,h,i,j]

                                            S = checkSum(inner, outer)
                                            #print(S)
                                            if S != False:
                                                if S not in L:
                                                    L.append(S)

    return findMax(L)

print(main())