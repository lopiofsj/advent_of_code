#!/usr/bin/env python3
"""Advent of code."""
#
# https://adventofcode.com/2019/day/4
#
import argparse


def _part_two(values):
    """An Elf just remembered one more important detail: the two adjacent
    matching digits are not part of a larger group of matching digits.

    Given this additional criterion, but still ignoring the range rule,
    the following are now true:

    * 112233 meets these criteria because the digits never decrease and all
      repeated digits are exactly two digits long.
    * 123444 no longer meets the criteria (the repeated 44 is part of a
      larger group of 444).
    * 111122 meets the criteria (even though 1 is repeated more than twice,
      it still contains a double 22).

    How many different passwords within the range given in your puzzle
    input meet all of the criteria?"""
    good = False

    # print(values)
    index = 0
    while index < len(values):
        v = values[index]
        counter = 0
        # print("index={}, value={}".format(index, v))
        for vv in values[index+1:]:
            # print('\t{}'.format(vv))
            if v == vv:
                counter += 1
            else:
                break
        if counter == 1:
            good = True
        # print("counter={}".format(counter))
        index = index + 1 + counter

    return good


def do_work():
    """
    You arrive at the Venus fuel depot only to discover it's protected by a
    password. The Elves had written the password on a sticky note, but someone
    threw it out.

    However, they do remember a few key facts about the password:

    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever
    increase or stay the same (like 111123 or 135679).
    Other than the range rule, the following are true:

    111111 meets these criteria (double 11, never decreases).
    223450 does not meet these criteria (decreasing pair of digits 50).
    123789 does not meet these criteria (no double).
    How many different passwords within the range given in your puzzle input
    meet these criteria?
    """

    range_lower = 273025
    range_upper = 767253

    valid_pws = 0
    part_two_valid_pws = 0

    # for v in test:
    for v in range(range_lower, range_upper + 1):
        # ones place
        a = int(v % 10)

        # tens place
        v = int(v/10)
        b = int(v % 10)

        # hundreds place
        v = int(v/10)
        c = int(v % 10)

        # thousands place
        v = int(v/10)
        d = int(v % 10)

        # ten-thousands place
        v = int(v/10)
        e = int(v % 10)

        # hundred-thousands place
        v = int(v/10)
        f = int(v % 10)

        # check for non-decreasing
        if a >= b >= c >= d >= e >= f:
            # check for consecutive digits
            if a == b or b == c or c == d or d == e or e == f:
                valid_pws += 1
                # check for part 2 validity
                rv = _part_two([a, b, c, d, e, f])
                if rv:
                    part_two_valid_pws += 1
                # else:
                #     print(orig_value)

    print("part one: valid passwords: {}".format(valid_pws))
    print("part two: valid passwords: {}".format(part_two_valid_pws))


###############################################################################
###############################################################################
###############################################################################
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="advent of code")
    # parser.add_argument('--file', '-f',
    #                     help="use file for data instead of STDIN")

    # args = parser.parse_args()

    # if args.file:
    #     input_files = [args.file, ]
    # else:
    #     input_files = ['-', ]

    # do_work(input_files)

    do_work()
