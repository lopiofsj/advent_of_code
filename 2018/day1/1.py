#!/usr/bin/env python3
#
# https://adventofcode.com/2018/day/1
#
# For example, if the device displays frequency changes of +1, -2, +3, +1,
# then starting from a frequency of zero, the following changes would occur:
#
# Current frequency  0, change of +1; resulting frequency  1.
# Current frequency  1, change of -2; resulting frequency -1.
# Current frequency -1, change of +3; resulting frequency  2.
# Current frequency  2, change of +1; resulting frequency  3.
# In this example, the resulting frequency is 3
#
# Read from STDIN

import fileinput

freq = 0

for line in fileinput.input():
    freq += int(line)

print(freq)
