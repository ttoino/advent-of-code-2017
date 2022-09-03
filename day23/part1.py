import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, defaultdict

with open("input") as inf, open("part1.out", "w+") as outf:
    registers = defaultdict(lambda: 0)
    result = 0
    ip = 0

    def get(r: str):
        return registers[r] if r.isalpha() else int(r)

    instructions = [a.strip().split() for a in inf]

    while len(instructions) > ip >= 0:
        match instructions[ip]:
            case ["set", x, y]:
                registers[x] = get(y)
            case ["sub", x, y]:
                registers[x] -= get(y)
            case ["mul", x, y]:
                registers[x] *= get(y)
                result += 1
            case ["jnz", x, y]:
                if get(x) != 0:
                    ip += get(y)
                    continue
        ip += 1

    outf.write(str(result))
