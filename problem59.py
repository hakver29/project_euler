def xor(a,b):
    M = []
    N = []
    O = []
    for i in range(8):
        M.append(a % 2)
        a = a - (a % 2)
        a = a / 2

    for i in range(8):
        N.append(b % 2)
        b = b - (b % 2)
        b = b / 2

    for i in range(8):
        if M[i] != N[i]:
            O.append(1)
        else:
            O.append(0)
            
    m = 0
    for i in range(8):
        m += O[i]*(2**i)
    return m
    
def encrypt(text,x,y,z):
    M = []
    for i in range(0,len(text)):
        if i % 3 == 0:
            M.append(xor(text[i],x))
        elif i % 3 == 1:
            M.append(xor(text[i],y))
        elif i % 3 == 2:
            M.append(xor(text[i],z))
    return M

def int_to_text(text):
    M = ''
    for i in text:
        M = M + chr(i)
    return M


def main():
    filename = "p059_cipher.txt"

    file = open(filename, "r")
    cipher = file.read()
    cipher = cipher.split(",")
    cipher = [int(i) for i in cipher]
    for x in range(97,123):
        for y in range(97,123):
            for z in range(97,123):
                X = encrypt(cipher,x,y,z)
                text = int_to_text(X)
                if "the" in text and "be" in text and "to" in text and "of" in text and "and" in text:
                    N = [x,y,z]

    S = 0
    X = encrypt(cipher, N[0], N[1], N[2])
    for j in X:
        S += j
    return S
