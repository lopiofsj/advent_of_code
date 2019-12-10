#!/usr/bin/env python3
#
# https://adventofcode.com/2018/day/1#part2
#
# You notice that the device repeats the same frequency change list over and
# over. To calibrate the device, you need to find the first frequency it
# reaches twice.
#
# For example, using the same list of changes above, the device would loop as
# follows:
#
# Current frequency  0, change of +1; resulting frequency  1.
# Current frequency  1, change of -2; resulting frequency -1.
# Current frequency -1, change of +3; resulting frequency  2.
# Current frequency  2, change of +1; resulting frequency  3.
# (At this point, the device continues from the start of the list.)
# Current frequency  3, change of +1; resulting frequency  4.
# Current frequency  4, change of -2; resulting frequency  2, which has
# already been seen.
# In this example, the first frequency reached twice is 2. Note that your
# device might need to repeat its list of frequency changes many times before
# a duplicate frequency is found, and that duplicates might be found while in
# the middle of processing the list.

#
# Read from STDIN

import fileinput

current_freq = 0
found = False
freqs = {current_freq: True}
prev = []

for line in fileinput.input():
    i = int(line)
    current_freq += i
    print("input: {} - current_freq: {}".format(i, current_freq))
    if current_freq in freqs:
        found = True
        break
    else:
        freqs[current_freq] = True
        prev.append(i)

print('*'*80)
while not found:
    for i in prev:
        current_freq += i
        if current_freq in freqs:
            found = True
            break
        else:
            freqs[current_freq] = True

print(found)
print(current_freq)
