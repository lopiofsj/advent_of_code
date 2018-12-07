#!/usr/bin/env python3
#
# https://adventofcode.com/2018/day/2
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
    #print("2's: {}, 3's: {}".format(found_2, found_3))


checksum = twos * threes
print("Checksum = {}".format(checksum))
