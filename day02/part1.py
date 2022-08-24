import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    outf.write(
        str(
            sum(
                max(i) - min(i) for i in (list(map(int,
                                                   i.strip().split()))
                                          for i in inf))))
