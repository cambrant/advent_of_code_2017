#!/usr/bin/env python

with open('day1_input.txt', 'r') as f:
    seq = f.read().strip()

sum = 0
last = ''
for digit in seq:
    if digit == last:
        sum += int(digit)
    last = digit

if last == seq[0]:
    sum += int(last)

print sum
