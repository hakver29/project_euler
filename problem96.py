def square_and_multiply(rest,base,power,modulo):
    if power == 1:
        return base*rest
    if power % 2 == 0:
        rest = rest
        base = (base**2) % modulo
        power = power / 2
        return square_and_multiply(rest,base,power,modulo)
    elif power % 2 == 1:
        rest = rest*base % modulo
        base = (base**2) % modulo
        power = (power - 1)/2
        return square_and_multiply(rest, base,power,modulo)

def main():
    base = 2
    power = 7830457
    modulo = 10000000000
    rest = 28433
    X = square_and_multiply(rest,base,power,modulo) % modulo
    X += 1
    return X
