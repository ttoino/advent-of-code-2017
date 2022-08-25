import itertools as it
from math import ceil, sqrt
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    n = int(inf.readline().strip())
    s = ceil(sqrt(n))
    s += s % 2 == 0
    i = (n - (s - 2)**2)
    i %= s**2 - (s - 2)**2
    outf.write(str(i))
