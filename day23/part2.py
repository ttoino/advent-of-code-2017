import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, defaultdict

with open("input") as inf, open("part2.out", "w+") as outf:
    h = 0
    for b in range(93 * 100 + 100000, 93 * 100 + 100000 + 17000 + 1, 17):
        for d in range(2, b):
            if b % d == 0:
                h += 1
                break

    outf.write(str(h))
