import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    buffer = [0]
    p = 0
    d = int(inf.readline().strip())

    for i in range(1, 2018):
        p += d
        p %= len(buffer)
        buffer.insert(p := p + 1, i)

    outf.write(str(buffer[p + 1]))
