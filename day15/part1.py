import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    a = int(inf.readline().strip().split()[-1])
    b = int(inf.readline().strip().split()[-1])
    s = 0

    for _ in range(40_000_000):
        a *= 16807
        a %= 2147483647
        b *= 48271
        b %= 2147483647
        s += a & 0xffff == b & 0xffff

    outf.write(str(s))
