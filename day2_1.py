#!/usr/bin/env python

with open('day2_input.txt', 'r') as f:
    rows = f.readlines()

sum = 0
for r in rows:
    cols = []
    for c in r.split():
        cols.append(int(c))
    cols = sorted(cols)

    sum += cols[-1] - cols[0]

print sum
