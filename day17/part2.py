import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, deque

with open("input") as inf, open("part2.out", "w+") as outf:
    l = 0
    p = 0
    d = int(inf.readline().strip())
    a = 0

    for i in range(1, 50_000_001):
        if (p := (p + d) % i) == 0:
            a = i
        p += 1

    outf.write(str(a))
