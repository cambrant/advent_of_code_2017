#!/usr/bin/env python

def divisable(cols):
    for c1 in cols:
        for c2 in cols:
            if c1 == c2:
                continue
            elif c1 % c2 == 0:
                return c1 / c2

with open('day2_input.txt', 'r') as f:
    rows = f.readlines()

sum = 0
for r in rows:
    cols = []
    for c in r.split():
        cols.append(int(c))

    sum += divisable(cols)

print sum
