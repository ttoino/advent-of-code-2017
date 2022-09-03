import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


def add_tuples(a, b):
    return tuple(i + j for i, j in zip(a, b))


with open("input") as inf, open("part1.out", "w+") as outf:
    infected = {(x, y)
                for y, l in enumerate(inf, start=-12)
                for x, c in enumerate(l.strip(), start=-12)
                if c == "#"}

    pos = (0, 0)
    dir = 0
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    result = 0

    for i in range(10000):
        dir += 1 + 2 * (pos not in infected)
        dir %= 4

        if pos in infected:
            infected.remove(pos)
        else:
            infected.add(pos)
            result += 1

        pos = add_tuples(pos, dirs[dir])

    outf.write(str(result))
