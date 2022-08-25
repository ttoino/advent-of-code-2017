import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    outf.write(
        str(
            sum(
                len(set(a)) == len(a)
                for a in (["".join(sorted(x))
                           for x in i.strip().split()]
                          for i in inf))))
