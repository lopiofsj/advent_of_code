#!/usr/bin/env python3
"""Advent of code."""
#
# https://adventofcode.com/2020/day/1
#
import fileinput
import argparse


def do_work(files):
    """Advent of code 2020, Day 1."""

    data = []
    for line in fileinput.input(files=files):
        data.append(int(line[:-1]))

    part_one(data)
    part_two(data)


def part_two(data):
    """ Find the three entries that sum to 2020 and then multiply those three
    numbers together.

    For example, suppose your expense report contained the following:

    1721
    979
    366
    299
    675
    1456
    In this list, the three entries that sum to 2020 are 979, 366, and 675.
    Multiplying them together produces the answer 241861950.
    """

    msg = "Part two answer: {}"

    for first_index, value in enumerate(data):
        for second_index, second_value in enumerate(data[first_index+1:]):
            for third_value in data[second_index + 1:]:
                if (value + second_value + third_value) == 2020:
                    product = (value * second_value * third_value)
                    print(msg.format(product))
                    return


def part_one(data):
    """ Find the two entries that sum to 2020 and then multiply those two
    numbers together.

    For example, suppose your expense report contained the following:

    1721
    979
    366
    299
    675
    1456
    In this list, the two entries that sum to 2020 are 1721 and 299.
    Multiplying them together produces 1721 * 299 = 514579,
    so the correct answer is 514579
    """

    msg = "Part one answer: {}"

    for index, value in enumerate(data):
        for second_value in data[index+1:]:
            if (value + second_value) == 2020:
                product = (value * second_value)
                print(msg.format(product))
                return


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
