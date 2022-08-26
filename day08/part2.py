import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, defaultdict

with open("input") as inf, open("part2.out", "w+") as outf:
    registers = defaultdict(lambda: 0)
    values = set()

    p = re.compile(r"(\w+) (inc|dec) (-?\d+) if ((\w+) [!<>=]=? -?\d+)")

    for i in inf:
        m = p.match(i)

        if eval(m[4].replace(m[5], f"registers['{m[5]}']")):
            registers[m[1]] += int(m[3]) * ((m[2] == "inc") - (m[2] == "dec"))

        values |= set(registers.values())

    outf.write(str(max(values)))
