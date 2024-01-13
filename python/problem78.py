M = 1000000
def main():
    recurrenceList = [1,1,2,3,5,7,11,15]

    nextStep = calculateNext(recurrenceList,len(recurrenceList)+1)
    while nextStep % 1000000 != 0:
        recurrenceList.append(nextStep)
        nextStep = calculateNext(recurrenceList, len(recurrenceList) + 1)
    print(len(recurrenceList))



def calculateNext(L, n):
    N = 0
    k = 1
    index = 0
    while index >= 0:
        index = n - (k * (3 * k - 1)) // 2 - 1
        if index >= 0:
            N += pow(-1, k - 1)*L[index]
        k = k + 1

    k = 1
    index = 0
    while index >= 0:
        index = n - (k * (3 * k + 1)) // 2 - 1
        if index >= 0:
            N += pow(-1, k - 1) * L[index]
        k = k + 1

    return N

main()