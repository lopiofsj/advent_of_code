#!/usr/bin/env python3
"""Advent of code."""
#
# https://adventofcode.com/2018/day5
#
# #The polymer is formed by smaller units which, when triggered, react with
# each other such that two adjacent units of the same type and opposite
# polarity are destroyed. Units' types are represented by letters; units'
# polarity is represented by capitalization. For instance, r and R are units
# with the same type but opposite polarity, whereas r and s are entirely
# different types and do not react.
#
# For example:
#
# In aA, a and A react, leaving nothing behind.
# In abBA, bB destroys itself, leaving aA. As above, this then destroys itself,
#   leaving nothing.
# In abAB, no two adjacent units are of the same type, and so nothing happens.
# In aabAAB, even though aa and AA are of the same type, their polarities
#   match, and so nothing happens.
# Now, consider a larger example, dabAcCaCBAcCcaDA:
#
# dabAcCaCBAcCcaDA  The first 'cC' is removed.
# dabAaCBAcCcaDA    This creates 'Aa', which is removed.
# dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
# dabCBAcaDA        No further actions can be taken.
# After all possible reactions, the resulting polymer contains 10 units.
#
# How many units remain after fully reacting the polymer you scanned?
#
# --- Part Two ---
#
# Time to improve the polymer.
#
# One of the unit types is causing problems; it's preventing the polymer from
# collapsing as much as it should. Your goal is to figure out which unit type
# is causing the most problems, remove all instances of it (regardless of
# polarity), fully react the remaining polymer, and measure its length.
#
# For example, again using the polymer dabAcCaCBAcCcaDA from above:
#
# Removing all A/a units produces dbcCCBcCcD. Fully reacting this polymer
#   produces dbCBcD, which has length 6.
# Removing all B/b units produces daAcCaCAcCcaDA. Fully reacting this polymer
#   produces daCAcaDA, which has length 8.
# Removing all C/c units produces dabAaBAaDA. Fully reacting this polymer
#   produces daDA, which has length 4.
# Removing all D/d units produces abAcCaCBAcCcaA. Fully reacting this polymer
#   produces abCBAc, which has length 6.
# In this example, removing all C/c units was best, producing the answer 4.
#
# What is the length of the shortest polymer you can produce by removing all
# units of exactly one type and fully reacting the result?
#
import fileinput
import argparse
import copy
import string


def part_1(line):
    prev_data = []
    current_data = []

    # first pass
    counter = 0
    while counter < len(line):
        c = line[counter]
        if c.isupper() and c.lower() == line[counter+1]:
            # print("skipping: {}".format(c))
            counter += 2
        elif c.islower() and c.upper() == line[counter+1]:
            # print("skipping: {}".format(c))
            counter += 2
        else:
            prev_data.append(c)
            counter += 1

    while current_data != prev_data:
        # print(prev_data)
        current_data = copy.deepcopy(prev_data)
        prev_data = []
        counter = 0
        while counter < len(current_data):
            c = current_data[counter]
            if c.isupper() and c.lower() == current_data[counter+1]:
                # print("skipping: {}".format(c))
                counter += 2
            elif c.islower() and c.upper() == current_data[counter+1]:
                # print("skipping: {}".format(c))
                counter += 2
            else:
                prev_data.append(c)
                counter += 1

    units = len(current_data[:-1])
    return units


def do_work(files):
    """For the data in the file(s), do the work of solving the puzzle."""
    for line in fileinput.input(files=files):
        pass
    units = part_1(line)
    print("Part 1: Units: {}".format(units))

    # Part 2
    letter = ''
    min_units = 100000000
    for c in string.ascii_lowercase:
        new_str = line.replace(c, '').replace(c.upper(), '')
        rv = part_1(new_str)
        if rv < min_units:
            min_units = rv
            letter = c
    print('Letter: {}, Units: {}'.format(letter, min_units))


###############################################################################
###############################################################################
###############################################################################
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="advent of code - day 5")
    parser.add_argument('--file', '-f',
                        help="use file for data instead of STDIN")

    args = parser.parse_args()

    if args.file:
        input_files = [args.file, ]
    else:
        input_files = ['-', ]

    do_work(input_files)
