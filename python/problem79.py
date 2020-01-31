import pandas as pd
import os


path = './p079_keylog.txt'

data = pd.read_csv(path, header=None)
print(data)

# First letter: [1,3,6,7]
# Only 7 is always first: 7
# Second letter: [1,2,3,6]
# 3 before 1
# 3 before 6
# 3 before 2
# Second letter: 3
# Third letter: [0, 1,2,6,7,8,9]
# 1 before 9 2 8 6 0
# Third letter: 1
# Fourth letter: [0,2,6,8,9]
# 6 before 0,2,8,9
# Fourth letter: 6
# Fifth letter: [0,2,8,9]
# 8 before 0
# 9 before 0
# 8 before 9
# 2 before 9
# 2 before 8
# Fifth letter: 2
# Sixth letter: [0,8,9]
# Remaining: 890
# Answer: 73162890

