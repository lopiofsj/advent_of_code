#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Advent of code."""
#
# https://adventofcode.com/2021
#
# Count the number of times a depth measurement increases from the previous
# measurement. (There is no measurement before the first measurement.)
#
import fileinput
import argparse


def do_work(files):
    """For the data in the file(s), do the work of solving the puzzle."""

    # part 1
    count = 0
    thelist = [int(x) for x in fileinput.input(files=files)]
    for i in range(len(thelist)):
        if i > 0:
            if thelist[i] > thelist[i-1]:
                count += 1
    print(f"Part 1: The count is {count}")

    count = 0
    for i in range(len(thelist)):
        if i > 2:
            if (thelist[i] + thelist[i-1] + thelist[i-2]) > (thelist[i-1] + thelist[i-2] + thelist[i-3]):
                count += 1
    print(f"Part 2: The count is {count}")

###############################################################################
###############################################################################
###############################################################################
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="advent of code")
    parser.add_argument('--file', '-f',
                        help="use file for data instead of STDIN")

    args = parser.parse_args()

    if args.file:
        input_files = [args.file, ]
    else:
        input_files = ['-', ]

    do_work(input_files)
