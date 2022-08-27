import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    layers = [tuple(map(int, i.strip().split(": "))) for i in inf]
    outf.write(str(sum(d * r for d, r in layers if d % (r * 2 - 2) == 0)))
