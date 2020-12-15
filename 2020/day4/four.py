#!/usr/bin/env python3
"""Advent of code."""
#
# https://adventofcode.com/2020/day/4
#
import fileinput
import argparse
import re

# expected fields
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
expected = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

hgt_re = re.compile(r"(?P<height>\d+)(?P<unit>(cm|in))")
hcl_re = re.compile(r"#(?P<value>[0-9abcedfABCDEF]{6}$)")
pid_re = re.compile(r'\d{9}$')

eye_colors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def _part_two(passport):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        return False

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        return False

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        return False

    # hgt (Height) - a number followed by either cm or in:
    found = hgt_re.match(passport['hgt'])
    if not found:
        return False
    h = int(found.group('height'))
    # If cm, the number must be at least 150 and at most 193.
    if 'cm' == found.group('unit'):
        if h < 150 or h > 193:
            return False
    # If in, the number must be at least 59 and at most 76.
    else:
        if h < 59 or h > 76:
            return False

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    found = hcl_re.match(passport['hcl'])
    if not found:
        return False

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if passport['ecl'] not in eye_colors:
        return False

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if not pid_re.match(passport['pid']):
        return False

    # cid (Country ID) - ignored, missing or not.

    # print(passport)
    return True


def do_work(files):
    """For the data in the file(s), do the work of solving the puzzle."""

    part_one_valid = 0
    part_two_valid = 0
    current_keys = []
    current_passport = {}
    for line in fileinput.input(files=files):
        # print(line[:-1])
        # not a new passport
        if len(line[:-1]) > 0:
            a = line[:-1].split(' ')
            for b in a:
                k, v = b.split(':')
                current_passport[k] = v
                # if k == 'cid':
                #     continue
                current_keys.append(k)
        else:
            # print(current_keys)
            if set(current_keys) >= expected:
                part_one_valid += 1
                if _part_two(current_passport):
                    part_two_valid += 1
            current_keys = []
            current_passport = {}

    # we have to see if there was a passport at the end of the file
    if current_keys:
        print(current_keys)
        if set(current_keys) >= expected:
            part_one_valid += 1
            if _part_two(current_passport):
                part_two_valid += 1

    print("Part one: valid = {}".format(part_one_valid))
    print("Part two: valid = {}".format(part_two_valid))


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
