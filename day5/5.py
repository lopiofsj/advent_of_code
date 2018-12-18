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
import fileinput
import argparse
import copy


def do_work(files):
    """For the data in the file(s), do the work of solving the puzzle."""

    prev_data = []
    current_data = []

    # first pass
    for line in fileinput.input(files=files):
        # print(line)
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
    print("Units: {}".format(units))


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
