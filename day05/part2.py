import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    jumps = [int(i.strip()) for i in inf]

    ip = 0
    for i in it.count():
        if ip >= len(jumps) or ip < 0:
            outf.write(str(i))
            break

        temp = ip
        ip += jumps[temp]
        jumps[temp] += (jumps[temp] < 3) - (jumps[temp] >= 3)
