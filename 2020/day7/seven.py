#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Advent of code."""
#
# https://adventofcode.com/2020
#
import fileinput
import argparse
import re
from pprint import pprint

BAG_RE = re.compile(r'(?P<bag>\w+ \w+) bags')


def do_work(files):
    """For the data in the file(s), do the work of solving the puzzle."""

    shinny_gold = []
    bags = {}

    for line in fileinput.input(files=files):
        print(line[:-1])
        found = BAG_RE.search(line)
        if not found:
            print("no bag found for line ({})".format(line))
            continue

        # we have the bag
        bag = found.group('bag')
        # print("BAG = ({})".format(bag))
        bags[bag] = {}

        # now find the bags contained
        if 'no other bags' in line:
            continue

        values = re.split(r'contain(s)?', line[:-1])
        for v in values[2:]:
            if 'shiny gold' in v:
                shinny_gold.append(bag)
    pprint(bags)
    pprint(shinny_gold)


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
