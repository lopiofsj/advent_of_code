#!/usr/bin/env python3
"""Advent of code."""
#
# https://adventofcode.com/2020/day/3
#
import fileinput
import argparse
from collections import namedtuple


# slope is right 3, down 1
RIGHT = 3
DOWN = 1

Slope = namedtuple("Slope", ("right", "down"))
SLOPES = [
    Slope(right=3, down=1),
    Slope(right=1, down=1),
    Slope(right=5, down=1),
    Slope(right=7, down=1),
    Slope(right=1, down=2),
]

SNOW = '.'
TREE = '#'


def do_work(files):
    """For the data in the file(s), do the work of solving the puzzle."""

    the_map = []
    for line in fileinput.input(files=files):
        the_map.append(line[:-1])

    total_lines = len(the_map)

    length_of_line = len(the_map[0])

    # part one
    the_slope = SLOPES[0]
    trees = _find_trees(the_map, total_lines, length_of_line, the_slope)
    print("Part One: Trees: {}".format(trees))

    # part two
    answer = 1
    for the_slope in SLOPES:
        trees = _find_trees(the_map, total_lines, length_of_line, the_slope)
        answer *= trees
    print("Part Two: Answer: {}".format(answer))


def _find_trees(the_map, total_lines, length_of_line, the_slope):

    trees = 0
    current_x = 0
    # for i in range(the_slope.down, total_lines):
    i = the_slope.down
    while i < total_lines:
        current_x += the_slope.right
        if current_x >= length_of_line:
            current_x -= length_of_line

        try:
            if the_map[i][current_x] == TREE:
                trees += 1
        except IndexError:
            msg = "len: {}, i: {}, current_x: {}, line: ({})"
            print(msg.format(length_of_line, i, current_x, the_map[i]))
        i += the_slope.down

    return trees


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
