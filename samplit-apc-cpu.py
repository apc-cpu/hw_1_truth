import sys
import random

if len(sys.argv) != 2:
    print("Usage: python samplit-apc-cpu.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        if random.random() < 0.01:
            print(line, end="")
