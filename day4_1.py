#!/usr/bin/env python

with open('day4_input.txt', 'r') as f:
    rows = f.readlines()

valid = 0

for r in rows:
    valid_phrase = True

    existing = []
    for word in r.strip().split():
        if word in existing:
            valid_phrase = False
        else:
            existing.append(word)

    if valid_phrase:
        valid += 1

print valid
