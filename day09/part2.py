import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    s = inf.readline().strip()

    garbage = 0
    score = 0
    depth = 0
    in_garbage = False
    i = 0
    while i < len(s):
        c = s[i]

        match c:
            case '!' if in_garbage:
                i += 1
            case '>' if in_garbage:
                in_garbage = False
            case _ if in_garbage:
                garbage += 1
            case '{':
                depth += 1
            case '}':
                score += depth
                depth -= 1
            case '<':
                in_garbage = True
        
        i += 1

    outf.write(str(garbage))
