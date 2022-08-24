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
                max(c) // min(c)
                for c in (c for i in inf
                          for c in it.combinations(map(int,
                                                       i.strip().split()), 2)
                          if max(c) % min(c) == 0))))
