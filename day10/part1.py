import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    l = list(range(256))
    skip_size = 0
    index = 0

    for i in inf.readline().strip().split(","):
        i = int(i)

        l[:i] = l[:i][::-1]

        l = l[(i + skip_size) % 256:] + l[:(i + skip_size) % 256]

        index += i + skip_size
        skip_size += 1

    index %= 256
    l = l[-index:] + l[:-index]

    outf.write(str(l[0] * l[1]))
