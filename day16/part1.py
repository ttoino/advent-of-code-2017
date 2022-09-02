import itertools as it
from string import ascii_lowercase
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    programs = list(ascii_lowercase[:16])

    for instruction in inf.readline().strip().split(","):
        match instruction[0], instruction[1:].split("/"):
            case "s", [x]:
                x = int(x)
                programs = programs[-x:] + programs[:-x]
            case "x", [a, b]:
                a, b = int(a), int(b)
                programs[a], programs[b] = programs[b], programs[a]
            case "p", [a, b]:
                a, b = programs.index(a), programs.index(b)
                programs[a], programs[b] = programs[b], programs[a]

    outf.write("".join(programs))
