#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Advent of code."""
#
# https://adventofcode.com/2023
#
import fileinput
import argparse


def do_work(files: (str)) -> None:
    """For the data in the file(s), do the work of solving the puzzle."""

    for line in fileinput.input(files=files):
        print(line)


###############################################################################
###############################################################################
###############################################################################
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="advent of code")
    parser.add_argument('files', nargs='1',
                        help="use file for data or '-' for STDIN")

    args = parser.parse_args()

    do_work(args.files)
