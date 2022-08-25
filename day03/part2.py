import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    d = {(0, 0): 1}
    n = int(inf.readline().strip())
    current = (0, 0)

    dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    while True:
        current = current[0] + 1, current[1]
        d[current] = sum(
            d.get((current[0] + dx, current[1] + dy), 0)
            for dx in range(-1, 2)
            for dy in range(-1, 2))
        if d[current] > n:
            outf.write(str(d[current]))
            exit()

        for i in range(4):
            while True:
                current = current[0] + dirs[i][0], current[1] + dirs[i][1]
                d[current] = sum(
                    d.get((current[0] + dx, current[1] + dy), 0)
                    for dx in range(-1, 2)
                    for dy in range(-1, 2))
                if d[current] > n:
                    outf.write(str(d[current]))
                    exit()

                if abs(current[0]) == abs(current[1]):
                    break
