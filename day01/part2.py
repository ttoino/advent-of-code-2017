import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    l = inf.readline().strip()
    outf.write(
        str(
            sum(
                int(a)
                for a, b in zip(l, l[len(l) // 2:] + l[:len(l) // 2])
                if a == b)))
