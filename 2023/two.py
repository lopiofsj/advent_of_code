#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Advent of code."""
#
# https://adventofcode.com/2023
#
import fileinput
import argparse
import re

game_id_re = re.compile(r'Game (?P<game_id>\d+)')
red_re = re.compile(r"(?P<red>\d+) red")
green_re = re.compile(r"(?P<green>\d+) green")
blue_re = re.compile(r"(?P<blue>\d+) blue")

def do_work(files: (str)) -> None:
    part_one(files)
    part_two(files)

def part_two(files: (str)) -> None:

    total = 0

    for line in fileinput.input(files=files):

        min_red = 0
        min_green = 0
        min_blue = 0

        # print(line[:-1])

        # which games could be played with
        # 12 red cubes, 13 green cubes, and 14 blue cubes

        # part 1
        match = game_id_re.search(line)
        if match:
            game_id = int(match.group("game_id"))
        else:
            continue

        # work with red
        for m in red_re.finditer(line):
            red = int(m.group('red'))
            if red > min_red:
                min_red = red
        # print(f"found min_red=({min_red})")

        # work with green
        for m in green_re.finditer(line):
            green = int(m.group('green'))
            if green > min_green:
                min_green = green
        # print(f"found min_green=({min_green})")

        # work with blue
        for m in blue_re.finditer(line):
            blue = int(m.group('blue'))
            if blue > min_blue:
                min_blue = blue
        # print(f"found min_blue=({min_blue})")

        cube = min_red * min_green * min_blue
        # print(f"cube = {cube}")
        total += cube

    print(f"Part 2: The total is {total}")

def part_one(files: (str)) -> None:
    """For the data in the file(s), do the work of solving the puzzle."""

    # sample line
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

    total = 0

    max_red = 12
    max_green = 13
    max_blue = 14

    for line in fileinput.input(files=files):

        broken = False

        # which games could be played with
        # 12 red cubes, 13 green cubes, and 14 blue cubes

        # part 1
        match = game_id_re.search(line)
        if match:
            game_id = int(match.group("game_id"))
        else:
            continue

        # work with red
        for m in red_re.finditer(line):
            red = int(m.group('red'))
            # print(f"found red=({m.group('red')})")
            if red <= 0 or red > max_red:
                # print('red is too large')
                broken = True
                break

        if broken:
            continue

        # work with green
        for m in green_re.finditer(line):
            green = int(m.group('green'))
            # print(f"found green=({m.group('green')})")
            if green <= 0 or green > max_green:
                # print('green is too large')
                broken = True
                break

        if broken:
            continue

        # work with blue
        for m in blue_re.finditer(line):
            blue = int(m.group('blue'))
            # print(f"found blue=({m.group('blue')})")
            if blue <= 0 or blue > max_blue:
                # print('blue is too large')
                broken = True
                break

        if broken:
            continue

        # if we're here then the values are all good
        total += game_id
        #print(f"game_id={game_id}, running total={total}")

    print(f"Part 1: The total is {total}")


###############################################################################
###############################################################################
###############################################################################
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="advent of code")
    parser.add_argument('files', nargs='*',
                        help="use file for data or '-' for STDIN")

    args = parser.parse_args()

    do_work(args.files)
