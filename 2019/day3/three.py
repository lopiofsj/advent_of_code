#!/usr/bin/env python3
"""Advent of code."""
#
# https://adventofcode.com/2019
#
import fileinput
import argparse


def _calc_hashes(directions):

    # Right = add to X
    # Left = subtract from X
    # Up = add to Y
    # down = subtract from Y
    print(directions[0][0], directions[0][1:])

    for pt in directions:
        print(pt[0], pt[1:])

    return {}


def do_work(files):
    """For the data in the file(s), do the work of solving the puzzle."""

    # for each path, record it's locations in a hash.
    # For example, {'1,0', '2,0', '2,1'}
    # then we can compare the hashes and find common keys.
    # the distance from the origin is just the addition of x+y
    routes = []

    for i, line in enumerate(fileinput.input(files=files)):
        data = line[:-1].split(',')
        routes.append(_calc_hashes(data))



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
