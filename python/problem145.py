
def isValid(n):
    n = str(n)
    #print(str(int(n[::-1])))
    if n == str(int(n[::-1]))[::-1]:
        return True
    else:
        return False



def check_odd_digit(n):
    n = str(n)
    for i in n:
        if int(i) % 2 == 0:
            return False
    return True

def main():
    S = 0
    for i in range(1,1000000000):
        if isValid(i):
            #print(i)
            int_i = str(i)
            i_rev = int_i[::-1]
            n = int(int_i) + int(i_rev)
            if check_odd_digit(n):
                S += 1

    print(S)

main()