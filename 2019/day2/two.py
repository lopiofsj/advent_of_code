#!/usr/bin/env python3
"""Advent of code."""
#
# https://adventofcode.com/2019
#
import fileinput
import argparse
from copy import deepcopy

OPCODES = {
    1: 'ADD_CODE',
    2: 'PRODUCT_CODE',
    99: 'END_CODE'
}


def _process_program(program):

    ADD_CODE = 1
    PRODUCT_CODE = 2
    END_CODE = 99
    JUMP = 4

    index = 0
    first_loc = second_loc = answer = 0
    answer_loc = 0
    while index < len(program):
        if program[index] == END_CODE:
            break

        first_loc = program[index + 1]
        second_loc = program[index + 2]
        answer_loc = program[index + 3]

        if program[index] == ADD_CODE:
            answer = program[first_loc] + program[second_loc]

        elif program[index] == PRODUCT_CODE:
            answer = program[first_loc] * program[second_loc]

        program[answer_loc] = answer

        index += JUMP

    return program[0]


def do_work(files):
    """For the data in the file(s), do the work of solving the puzzle."""

    for line in fileinput.input(files=files):
        inputs = [int(x) for x in line[:-1].split(',')]
        orig_inputs = deepcopy(inputs)

        # part one
        # replacements!
        inputs[1] = 12
        inputs[2] = 2
        result = _process_program(inputs)
        print(result)

        # part two
        for one in range(0, 100):
            for two in range(0, 100):
                new_inputs = deepcopy(orig_inputs)
                new_inputs[1] = one
                new_inputs[2] = two
                result = _process_program(new_inputs)
                if result == 19690720:
                    print(one, two, result)
                    break



###############################################################################
###############################################################################
###############################################################################
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="advent of code")
    parser.add_argument('--file', '-f',
                        help="use file for data instead of STDIN",
                        default='testintput.txt')

    args = parser.parse_args()

    if args.file:
        input_files = [args.file, ]
    else:
        input_files = ['-', ]

    do_work(input_files)
