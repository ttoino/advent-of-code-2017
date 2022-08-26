import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    p = re.compile(r"(\w+) \((\d+)\)(?: -> ((?:\w+,? ?)+))?")

    towers = list(
        zip(*[g for i in inf if (g := p.match(i).groups())[2] is not None]))
    names = set(towers[0])
    children = set(sum((i.split(", ") for i in towers[2]), []))
    outf.write(next(iter(names - children)))