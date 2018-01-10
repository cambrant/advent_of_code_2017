#!/usr/bin/env python

with open('day1_input.txt', 'r') as f:
    seq = f.read().strip()

sum = 0

for index, digit in enumerate(seq):
    match = (index + (len(seq) / 2))
    if match >= len(seq):
        match -= len(seq)

    if digit == seq[match]:
        sum += int(digit)

print sum
