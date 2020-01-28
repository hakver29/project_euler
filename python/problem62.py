def main():
    cubes = [''.join(sorted(str(i**3))) for i in range(1,10000)]
    cubes = sorted(cubes)

    yolo = []
    for i in range(len(cubes)-3):
        if cubes[i] == cubes[i+1] and cubes[i+1] == cubes[i+2] and cubes[i+2] == cubes[i+3] and cubes[i+3] == cubes[i+4]:
            yolo.append(cubes[i])

    for i in range(1,10000):
        x = ''.join(sorted(str(i**3)))
        for j in yolo:
            if x == j:
                return i**3

print(main())