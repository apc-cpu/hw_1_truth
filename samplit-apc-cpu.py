import sys
import random

filename = sys.argv[1]

with open(filename, "r") as f:
    # Randomly sample approximately 1% of lines
    for line in f:
        if random.random() < 0.01:
            print(line, end="")