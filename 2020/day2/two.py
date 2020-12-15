#!/usr/bin/env python3
"""Advent of code."""
#
# https://adventofcode.com/2020/day/2
#
import fileinput
import argparse


def do_work(files):
    """For the data in the file(s), do the work of solving the puzzle."""

    data = []
    for line in fileinput.input(files=files):
        data.append(line[:-1])

    part_one(data)
    part_two(data)


def part_two(data):
    """
    Each policy actually describes two positions in the password, where
    1 means the first character, 2 means the second character, and so on.
    (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
    Exactly one of these positions must contain the given letter.
    Other occurrences of the letter are irrelevant for the
    purposes of policy enforcement.

    Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
    How many passwords are valid according to the new interpretation of the
    policies?
    """

    valid_pws = 0
    for line in data:
        # split up each line into several parts
        # the line - 1-3 a: abcde
        # min = 1
        # max = 3
        # letter = a
        # password = abcde
        (the_range, foo, password) = line.split(' ')
        (a, b) = the_range.split('-')
        letter = foo[:-1]
        first_pos = int(a) - 1
        second_pos = int(b) - 1

        if letter == password[first_pos] and letter != password[second_pos]:
            valid_pws += 1
        elif letter != password[first_pos] and letter == password[second_pos]:
            valid_pws += 1

    print("Part two: valid passwords = {}".format(valid_pws))


def part_one(data):
    """
    To try to debug the problem, they have created a list (your puzzle input)
    of passwords (according to the corrupted database) and the corporate
    policy when that password was set.

    For example, suppose you have the following list:

    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc
    Each line gives the password policy and then the password. The password
    policy indicates the lowest and highest number of times a given letter
    must appear for the password to be valid. For example, 1-3 a means that
    the password must contain a at least 1 time and at most 3 times.

    In the above example, 2 passwords are valid. The middle password, cdefg,
    is not; it contains no instances of b, but needs at least 1. The first and
    third passwords are valid: they contain one a or nine c, both within the
    limits of their respective policies.

    How many passwords are valid according to their policies?
    """

    valid_pws = 0
    for line in data:
        # split up each line into several parts
        # the line - 1-3 a: abcde
        # min = 1
        # max = 3
        # letter = a
        # password = abcde
        (the_range, the_letter, password) = line.split(' ')
        (range_min, range_max) = the_range.split('-')
        letter = the_letter[:-1]

        count = len(password.split(letter)) - 1
        if int(range_min) <= count <= int(range_max):
            valid_pws += 1

    print("Part one: valid passwords = {}".format(valid_pws))


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
