#!/usr/bin/env python3
#
# https://adventofcode.com/2018/day/2
# Confident that your list of box IDs is complete, you're ready to find the
# boxes full of prototype fabric.
#
# The boxes will have IDs which differ by exactly one character at the same
# position in both strings. For example, given the following box IDs:
#
# abcde
# fghij
# klmno
# pqrst
# fguij
# axcye
# wvxyz
# The IDs abcde and axcye are close, but they differ by two characters (the
# second and fourth). However, the IDs fghij and fguij differ by exactly one
# character, the third (h and u). Those must be the correct boxes.
#
# What letters are common between the two correct box IDs? (In the example
# above, this is found by removing the differing character from either ID,
# producing fgij.)
#
#
#
# Read from STDIN

import fileinput
import sys

lines = []


# Get the input
for line in fileinput.input():
    lines.append(line[:-1])


# Brute force, we'll traverse the list twice.
for one in lines:
    for two in lines:
        # find any character-by-character differences
        diffs = [i for i in range(len(one)) if one[i] != two[i]]
        # if we found only 1 difference, we're in!
        if len(diffs) == 1:
            # now we need to print the string, minus the rouge character
            for i in range(len(one)):
                if i in diffs:
                    continue
                print(one[i], end='')
            print('')
            sys.exit(0)
