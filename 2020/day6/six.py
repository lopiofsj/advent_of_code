#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Advent of code."""
#
# https://adventofcode.com/2020
#
import fileinput
import argparse


def _part_two(all_answers):
    num_peeps = 0
    everyone = 0
    answers = {}
    # print(all_answers)
    for a in all_answers:
        num_peeps += 1
        for c in a:
            if c not in answers:
                answers[c] = 0
            answers[c] += 1
    # print(answers)

    for k, v in answers.items():
        if v == num_peeps:
            everyone += 1

    return everyone


def do_work(files):
    """For the data in the file(s), do the work of solving the puzzle."""

    all_answers = []
    part_2_answers = []
    anyone_yes = 0
    everyone_yes = 0
    for line in fileinput.input(files=files):
        if len(line[:-1]) > 0:
            part_2_answers.append(line[:-1])
            for c in line[:-1]:
                all_answers.append(c)
        else:
            everyone_yes += _part_two(part_2_answers)
            anyone_yes += len(set(all_answers))
            all_answers = []
            part_2_answers = []

    if all_answers:
        anyone_yes += len(set(all_answers))
    if part_2_answers:
        everyone_yes += _part_two(part_2_answers)

    print("Part one: Total yeses = {}".format(anyone_yes))
    print("Part two: Total yeses = {}".format(everyone_yes))


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
