import numpy as np

with open("./wmt.txt.fixed", 'r') as wmt:
    print()
    print(np.random.choice(wmt.readlines()))