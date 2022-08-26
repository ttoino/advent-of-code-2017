import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


def add_tuples(a, b):
    return tuple(i + j for i, j in zip(a, b))


with open("input") as inf, open("part2.out", "w+") as outf:
    current = 0, 0, 0
    furthest = 0

    dirs = {
        "n": (0, -1, 1),
        "ne": (1, -1, 0),
        "se": (1, 0, -1),
        "s": (0, 1, -1),
        "sw": (-1, 1, 0),
        "nw": (-1, 0, 1)
    }

    for d in inf.readline().strip().split(","):
        current = add_tuples(current, dirs[d])
        furthest = max(furthest,
                       (abs(current[0]) + abs(current[1]) + abs(current[2])) //
                       2)

    outf.write(str(furthest))
