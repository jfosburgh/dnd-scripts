import numpy as np

wmt  = {}

with open("./wmt.txt", 'r') as inf:
    with open("./wmt.txt.fixed", 'w') as outf:
        for line in inf.readlines():
            parts = line.split(" ")
            number = parts[0]
            if len(number) ==  5:
                number = number[1:]
            effect = " ".join(parts[1:])
            wmt[number] = effect
            outf.write("{} {}".format(number, effect))

np.save("wmt", wmt)