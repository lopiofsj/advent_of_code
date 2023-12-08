#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Advent of code."""
#
# https://adventofcode.com/2023
#
import fileinput
import argparse
import re

NUMBER_STR = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
NUMBER_DIGIT = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def do_work(files):
    """For the data in the file(s), do the work of solving the puzzle."""

    part_1_total = part_2_total = 0

    for line in fileinput.input(files=files):
        
        # part one
        first = last = None
        for c in line:
            if re.search(r'\d', c):
                if not first:
                    # the first and last could be the same
                    first = last = int(c)
                else:
                    last = int(c)

        # print(f"line: ({line[:-1]}), first={first}, last={last}")
        if first and last:
            # print(f"part1_step={first*10 + last}")
            part_1_total = part_1_total + first*10 + last 

        # part two
        first2 = last2 = 0
        first_index = last_index = -1
        # TODO: need to account for the number appearing AGAIN. Use rfind or find but at the new index.
        for i, n in enumerate(NUMBER_STR):
            try:
                idx = line.index(n)
                if first_index == -1:  # nothing found yet
                    first_index = last_index = idx
                    first2 = last2 = i+1  # need to account for zero based
                elif idx < first_index:  # already have something, update
                    first_index = idx
                    first2 = i+1  # need to account for zero based
                elif idx > last_index:  # already have something, update
                    last_index = idx
                    last2 = i+1  # need to account for zero based

                # now check if the number reappears
                ridx = line.rfind(n, idx)
                if ridx > last_index:
                    last_index = ridx
                    last2 = i+1  # need to account for zero based

            except ValueError:
                pass
        for i, n in enumerate(NUMBER_DIGIT):
            try:
                idx = line.index(n)
                if first_index == -1:  # nothing found yet
                    first_index = last_index = idx
                    first2 = last2 = i+1  # need to account for zero based
                elif idx < first_index:  # already have something, update
                    first_index = idx
                    first2 = i+1  # need to account for zero based
                elif idx > last_index:  # already have something, update
                    last_index = idx
                    last2 = i+1  # need to account for zero based

                # again, check if the number reappears
                ridx = line.rfind(n, idx)
                if ridx > last_index:
                    last_index = ridx
                    last2 = i+1  # need to account for zero based
            except ValueError:
                pass

        if first2 and last2:
            # print(f"part2_step={first2*10 + last2}, indicies, {first_index}, {last_index}")
            part_2_total = part_2_total + first2*10 + last2


    print(f"part_1_total: {part_1_total}")
    print(f"part_2_total: {part_2_total}")



###############################################################################
###############################################################################
###############################################################################
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="advent of code")
    parser.add_argument('files', nargs='*',
                        help="use file for data or '-' for STDIN")

    args = parser.parse_args()

    do_work(args.files)
