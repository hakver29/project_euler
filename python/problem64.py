import math

def isIrrational(N):
    return int(math.sqrt(N)) != math.sqrt(N)

def getInitialValue(N):
    return [int(math.sqrt(N)), 1, int(math.sqrt(N))]

def isDivisible(a,b):
    if int(a/b) == a/b:
        return True
    else:
        return False

def getNextResidue(denominator, residue, N):
    common_denonminator = math.gcd(N - residue**2, denominator)

    if isDivisible(N - residue**2, denominator):
        newDenominator = int((N - residue**2)/denominator)
    else:
        newDenominator = int((N - residue**2)/common_denonminator)

    wholeNumber = int((denominator * (math.sqrt(N) + residue))/(N - residue**2))

    newResidue = abs(residue - newDenominator*wholeNumber)

    return [newDenominator, newResidue, wholeNumber]

def findSubstring(string):
    foundPeriods = {}

    for x in range(len(string)):
        #Tested substring
        substring = string[0:len(string)-x]
        #Frequency count
        occurence_count = string.count(substring)

        #Make a comparaison to original string
        if substring  * occurence_count in string:
            foundPeriods[occurence_count] = substring

    if foundPeriods == {}:
        return ''

    return foundPeriods[max(foundPeriods.keys())]

def checkPeriod(N):
    sequence = ''
    [wholeNumber, denominator, residue] = getInitialValue(N)
    i = 1
    maxNumber = 100
    while i < maxNumber:
        [denominator, residue, wholeNumber] = getNextResidue(denominator, residue, N)
        sequence += str(wholeNumber)
        i += 1
    #print(sequence, findSubstring(sequence))
    #print(sequence)
    return len(findSubstring(sequence))

#print(checkPeriod(13))

def main():
    S = 0
    for i in range(2,10001):
        if isIrrational(i) and checkPeriod(i) % 2 == 1:
            S += 1
    return S

#print(checkPeriod(19))
print(main())