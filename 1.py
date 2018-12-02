#!/usr/bin/env python3

import fileinput

freq = 0

for line in fileinput.input():
    freq += int(line)

print(freq)
