import math

best_area = 0
best_solution = float('inf')
N = 2000000

for i in range(2,1000):
    for j in range(2,1000):

        rectangles = (i*j) * (i*j - i - j + 1) / 4
        if abs(rectangles - N) < best_solution:
            best_area = (i-1)*(j-1)
            best_solution = abs(rectangles - N)

print(best_area)