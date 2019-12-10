#!/usr/bin/env python3
#
# https://adventofcode.com/2018/day/2
#
# To make sure you didn't miss any, you scan the likely candidate boxes again,
# counting the number that have an ID containing exactly two of any letter and
# then separately counting those with exactly three of any letter. You can
# multiply those two counts together to get a rudimentary checksum and compare
# it to what your device predicts.
#
# For example, if you see the following box IDs:
#
# abcdef contains no letters that appear exactly two or three times.
# bababc contains two a and three b, so it counts for both.
# abbcde contains two b, but no letter appears exactly three times.
# abcccd contains three c, but no letter appears exactly two times.
# aabcdd contains two a and two d, but it only counts once.
# abcdee contains two e.
# ababab contains three a and three b, but it only counts once.
# Of these box IDs, four of them contain a letter which appears exactly twice,
# and three of them contain a letter which appears exactly three times.
# Multiplying these together produces a checksum of 4 * 3 = 12.
#
# Read from STDIN

import fileinput

twos = threes = 0


for line in fileinput.input():
    letters = {}
    found_2 = found_3 = False
    for l in line:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1

    for v in letters.values():
        if v == 2 and not found_2:
            found_2 = True
        if v == 3 and not found_3:
            found_3 = True

    if found_2:
        twos += 1
    if found_3:
        threes += 1

checksum = twos * threes
print("Checksum = {}".format(checksum))
