import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    layers = [tuple(map(int, i.strip().split(": "))) for i in inf]

    for i in it.count():
        if sum((d + i) % (r * 2 - 2) == 0 for d, r in layers) == 0:
            outf.write(str(i))
            break
