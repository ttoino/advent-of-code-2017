import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


def add_tuples(a, b):
    return tuple(i + j for i, j in zip(a, b))


with open("input") as inf, open("part2.out", "w+") as outf:
    fl = inf.readline().removesuffix("\n")
    w = len(fl)
    pos = (fl.index("|"), 0)
    dir = 0
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    map = "".join(i.removesuffix("\n") for i in inf)
    h = len(map) // w
    result = ""
    steps = 1

    def get(p):
        return map[p[0] + p[1] * w]

    while 0 <= pos[0] < w and 0 <= pos[1] < h:
        c = get(pos)

        if c.isalpha():
            result += c
        if c == "+":
            dir -= 1 if get(add_tuples(pos, dirs[dir - 1])) != " " else 3
            dir %= 4
        if c == " ":
            break

        pos = add_tuples(pos, dirs[dir])
        steps += 1

    outf.write(str(steps))
