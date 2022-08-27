import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    a = int(inf.readline().strip().split()[-1])
    b = int(inf.readline().strip().split()[-1])
    s = 0

    for i in range(5_000_000):
        print(f"{i}/5000000", end='\r')
        while True:
            a *= 16807
            a %= 2147483647
            if a % 4 == 0:
                break
        while True:
            b *= 48271
            b %= 2147483647
            if b % 8 == 0:
                break
        s += a & 0xffff == b & 0xffff

    outf.write(str(s))
