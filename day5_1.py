#!/usr/bin/env python

lines = []

with open('day5_input.txt', 'r') as f:
    for line in f.readlines():
        lines.append(int(line.strip()))

current_address = 0
number_of_instructions = len(lines)

step_count = 0
try:
    while True:
        next_address = current_address + lines[current_address]
        lines[current_address] += 1
        current_address = next_address
        step_count += 1
except:
    print step_count
