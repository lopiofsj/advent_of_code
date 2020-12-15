#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Advent of code."""
#
# https://adventofcode.com/2020/day/5
#
#
# For example, consider just the first seven characters of FBFBBFFRLR:
#
# Start by considering the whole range, rows 0 through 127.
# F means to take the lower half, keeping rows 0 through 63.
# B means to take the upper half, keeping rows 32 through 63.
# F means to take the lower half, keeping rows 32 through 47.
# B means to take the upper half, keeping rows 40 through 47.
# B keeps rows 44 through 47.
# F keeps rows 44 through 45.
# The final F keeps the lower of the two, row 44.
# The last three characters will be either L or R; these specify exactly one
# of the 8 columns of seats on the plane (numbered 0 through 7). The same
# process as above proceeds again, this time with only three steps. L means
# to keep the lower half, while R means to keep the upper half.
#
# For example, consider just the last 3 characters of FBFBBFFRLR:
#
# Start by considering the whole range, columns 0 through 7.
# R means to take the upper half, keeping columns 4 through 7.
# L means to take the lower half, keeping columns 4 through 5.
# The final R keeps the upper of the two, column 5.
# So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.
#
# Every seat also has a unique seat ID: multiply the row by 8, then add the
# column. In this example, the seat has ID 44 * 8 + 5 = 357.
# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820
import fileinput
import argparse


COLUMNS = {
    'LLL': 0,
    'LLR': 1,
    'LRL': 2,
    'LRR': 3,
    'RLL': 4,
    'RLR': 5,
    'RRL': 6,
    'RRR': 7
}


def do_work(files):
    """For the data in the file(s), do the work of solving the puzzle."""

    rows = [0] * (128 * 8)
    seats = []
    for line in fileinput.input(files=files):
        seats.append(line[:-1])

    highest_seat_id = 0
    for seat in seats:
        rowstr = seat[0:7]
        columnstr = seat[7:11]
        row = int(rowstr.replace('F', '0').replace('B', '1'), 2)
        column = COLUMNS[columnstr]
        temp_seat_id = row + column
        rows[temp_seat_id] = 1
        seat_id = (row * 8) + column
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

    print("Part One: Highest Seat Id={}".format(highest_seat_id))
    print(rows)


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
