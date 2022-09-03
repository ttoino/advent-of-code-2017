import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, defaultdict


def add_tuples(a, b):
    return tuple(i + j for i, j in zip(a, b))


with open("input") as inf, open("part2.out", "w+") as outf:
    nodes = defaultdict(lambda: 3, (((x, y), 1)
                                    for y, l in enumerate(inf, start=-12)
                                    for x, c in enumerate(l.strip(), start=-12)
                                    if c == "#"))

    pos = (0, 0)
    dir = 0
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    result = 0

    for i in range(10000000):
        print(f"{i/100000:2.0f}%", end="\r")

        dir += nodes[pos]
        dir %= 4

        nodes[pos] += 1
        nodes[pos] %= 4
        result += nodes[pos] == 1

        pos = add_tuples(pos, dirs[dir])

    outf.write(str(result))
