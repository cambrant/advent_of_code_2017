#!/usr/bin/env python

def find_anagram(word1, word2):
    return (sorted(word1) == sorted(word2))

with open('day4_input.txt', 'r') as f:
    rows = f.readlines()

valid = 0

for r in rows:
    valid_phrase = True

    existing = []
    for word in r.strip().split():
        if word in existing:
            valid_phrase = False
            break
        else:
            existing.append(word)

    for word1 in r.strip().split():
        for word2 in r.strip().split():
            if word1 == word2:
                continue

            if find_anagram(word1, word2):
                valid_phrase = False

    if valid_phrase:
        valid += 1

print valid
