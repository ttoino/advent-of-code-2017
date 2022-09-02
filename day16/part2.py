import itertools as it
from string import ascii_lowercase
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    programs = list(ascii_lowercase[:16])
    instructions = inf.readline().strip().split(",")
    s = []

    for i in range(1_000_000_000):
        if programs in s:
            outf.write("".join(s[1_000_000_000 % i]))
            exit()

        s.append(programs[:])

        for instruction in instructions:
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
