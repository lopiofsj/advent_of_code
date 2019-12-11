#!/usr/bin/env python3
"""Advent of code."""
#
# https://adventofcode.com/2019
#
import fileinput
import argparse
from math import floor


def do_work(files):
    """For the data in the file(s), do the work of solving the puzzle."""
    total_fuel = 0

    for line in fileinput.input(files=files):
        mass = int(line[:-1])
        if mass < 6:
            continue
        total_fuel += floor(mass/3) - 2

    print("Part 1: Total Fuel = {}".format(total_fuel))

    # Part 2
    total_fuel = 0
    for line in fileinput.input(files=files):
        mass = int(line[:-1])
        if mass < 6:
            continue
        fuel_mass = floor(mass/3) - 2
        total_fuel += fuel_mass
        # print("Mass: {}, fuel_mass: {}, total_fuel: {}".format(mass, fuel_mass, total_fuel))

        remaining_fuel = fuel_mass
        remaining_fuel = floor(remaining_fuel / 3) - 2
        while remaining_fuel > 0:
            total_fuel += remaining_fuel
            # print("remaining_fuel: {}, total_fuel: {}".format(remaining_fuel, total_fuel))
            remaining_fuel = floor(remaining_fuel / 3) - 2

    print("Part 2: Total Fuel = {}".format(total_fuel))


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
