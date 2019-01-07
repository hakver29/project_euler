# Assume here that both base and power are restricted by 200
# Remains to show that this is the case

def digits(m):
    m = list(str(m))
    return len(m)

def main():
    S = 0
    for base in range(1,200):
        for power in range(1,200):
            X = base**power
            dgts = digits(X)
            if dgts == power:
                S += 1
    return S
