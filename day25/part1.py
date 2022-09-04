import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    on = set()
    pos = 0
    state = 0
    states = (((1, 1, 1), (0, -1, 1)), ((1, -1, 2), (0, 1, 4)),
              ((1, 1, 4), (0, -1, 3)), ((1, -1, 0), (1, -1, 0)),
              ((0, 1, 0), (0, 1, 5)), ((1, 1, 4), (1, 1, 0)))

    for i in range(12861455):
        v, d, s = states[state][pos in on]
        if v:
            on.add(pos)
        else:
            on.discard(pos)
        pos += d
        state = s

    outf.write(str(len(on)))
