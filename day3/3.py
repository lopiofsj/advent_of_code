#!/usr/bin/env python3
"""Advent of code Day 3 Part 1."""
# https://adventofcode.com/2018/day/3
#
# The problem is that many of the claims overlap, causing two or more claims
# to cover part of the same areas. For example, consider the following claims:
#
# #1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2
# Visually, these claim the following areas:
#
# ........
# ...2222.
# ...2222.
# .11XX22.
# .11XX22.
# .111133.
# .111133.
# ........
# The four square inches marked with X are claimed by both 1 and 2. (Claim 3,
# while adjacent to the others, does not overlap either of them.)
#
# If the Elves all proceed with their own plans, none of them will have enough
# fabric. How many square inches of fabric are within two or more claims?

import fileinput
import argparse
import re


def do_work(files):
    """For the data in the file(s), do the work of solving the puzzle."""
    squares = []
    total = 0
    matches = set()
    unique_id = -1

    pattern = r"#\d+ @ (?P<from_x>\d+),(?P<from_y>\d+): (?P<x_len>\d+)x(?P<y_len>\d+)"  # noqa: E501
    line_re = re.compile(pattern)

    # for each line, we'll compute the x,y tuples for each rectangle
    for line in fileinput.input(files=files):
        rv = line_re.search(line)
        if rv:
            xbegin = int(rv.group('from_x')) + 1
            xend = int(rv.group('from_x')) + int(rv.group('x_len'))
            ybegin = int(rv.group('from_y')) + 1
            yend = int(rv.group('from_y')) + int(rv.group('y_len'))
            single_square = []
            for x in range(xbegin, xend+1):
                for y in range(ybegin, yend+1):
                    single_square.append((x, y))

            squares.append(single_square)

    # Now go through the sets and see if any overlap
    # but we don't need to go through the last one because it would have been
    # reviewed by all the prevous set.
    print('*'*80)
    for counter, first in enumerate(squares[:-1]):
        # increase the counter by one because we don't need to check the
        # current set against itself.
        for second_counter, second in enumerate(squares[counter+1:]):
            # now find any points that are in both sets
            local_match = set(first) & set(second)
            if local_match:
                # but we also don't want to double count squares
                unique_match = local_match - matches
                # now we have squares that are unique to the 2 sets
                total += len(unique_match)
                # and add the points to the overall list so they're
                # not double counted.
                matches |= unique_match
        if not set(first) & matches:
            unique_id = counter + 1
    if unique_id == -1:
        unique_id = len(squares)

    print("Total: {}".format(total))
    print("Total: {}, Unique Id: {}".format(total, unique_id))


###############################################################################
###############################################################################
###############################################################################
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="day 3 part 1")
    parser.add_argument('--file', '-f',
                        help="use file for data instead of STDIN")

    args = parser.parse_args()

    if args.file:
        input_files = [args.file, ]
    else:
        input_files = ['-', ]

    do_work(input_files)
