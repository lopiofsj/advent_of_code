#!/usr/bin/env python3
"""Advent of code Day 4."""
#
# https://adventofcode.com/2018/day4
#
# For example, consider the following records, which have already been
# organized into chronological order:
#
# [1518-11-01 00:00] Guard #10 begins shift
# [1518-11-01 00:05] falls asleep
# [1518-11-01 00:25] wakes up
# [1518-11-01 00:30] falls asleep
# [1518-11-01 00:55] wakes up
# [1518-11-01 23:58] Guard #99 begins shift
# [1518-11-02 00:40] falls asleep
# [1518-11-02 00:50] wakes up
# [1518-11-03 00:05] Guard #10 begins shift
# [1518-11-03 00:24] falls asleep
# [1518-11-03 00:29] wakes up
# [1518-11-04 00:02] Guard #99 begins shift
# [1518-11-04 00:36] falls asleep
# [1518-11-04 00:46] wakes up
# [1518-11-05 00:03] Guard #99 begins shift
# [1518-11-05 00:45] falls asleep
# [1518-11-05 00:55] wakes up
#
# Timestamps are written using year-month-day hour:minute format. The guard
# falling asleep or waking up is always the one whose shift most recently
# started. Because all asleep/awake times are during the midnight hour
# (00:00 - 00:59), only the minute portion (00 - 59) is relevant for those
# events.
#
#
# If you can figure out the guard most likely to be asleep at a specific time,
# you might be able to trick that guard into working tonight so you can have
# the best chance of sneaking in. You have two strategies for choosing the
# best guard/minute combination.
#
# Strategy 1: Find the guard that has the most minutes asleep. What minute
# does that guard spend asleep the most?
#
# In the example above, Guard #10 spent the most minutes asleep, a total of
# 50 minutes (20+25+5), while Guard #99 only slept for a total of 30 minutes
# (10+10+10). Guard #10 was asleep most during minute 24 (on two days,
# whereas any other minute the guard was asleep was only seen on one day).
#
# While this example listed the entries in chronological order, your entries
# are in the order you found them. You'll need to organize them before they
# can be analyzed.
#
# What is the ID of the guard you chose multiplied by the minute you chose?
# (In the above example, the answer would be 10 * 24 = 240.)

#
# ASSUME INPUT IS SORTED
#


import fileinput
import argparse


class Guard(object):

    def __init__(self):
        self.total = 0
        self.minutes = [0] * 60


def do_work(files):
    """For the data in the file(s), do the work of solving the puzzle."""

    guards = {}
    begin_sleep = 0
    gid = -1

    for line in fileinput.input(files=files):
        # Index - What
        # 0 - [Year-Month-Day
        # 1 - Hour:Minute]
        # 2 - (Guard | falls | wakes)
        # 3 - (#id | asleep | up)
        data = line.split(' ')
        if 'Guard' in data[2]:
            gid = data[3][1:]  # drop the leading '#'
            if gid not in guards:
                    guards[gid] = Guard()
        elif 'falls' in data[2]:
            # get the minute and strip off the trailing ']'
            begin_sleep = int(data[1].split(':')[1][:-1])
        elif 'wakes' in data[2]:
            # get the minute and strip off the trailing ']'
            end_sleep = int(data[1].split(':')[1][:-1])
            # now calculate the time asleep
            guards[gid].total += (end_sleep - begin_sleep)
            # and keep track of which of the minutes the guard is asleep
            i = begin_sleep
            while i < end_sleep:
                guards[gid].minutes[i] += 1
                i += 1
            begin_sleep = end_sleep = -1

    # used to keep track of who we should target
    max_minute = max_sleep = -1
    max_gid = '-1'
    for k, v in guards.items():
        guard_max_minute = v.minutes.index(max(v.minutes))
        s = "GID: {:>5s}, Total Asleep: {:4d}, Max Minute: {:2d}"
        print(s.format(k, v.total, guard_max_minute))
        if max_sleep < v.total:
            max_minute = guard_max_minute
            max_sleep = v.total
            max_gid = k

    print('*' * 10)
    answer = int(max_gid) * max_minute
    s = "Answer: {:5d}, GID: {:>4s}, Total Asleep: {:4d}, Max Minute: {:2d}"
    print(s.format(answer, max_gid, max_sleep, max_minute))


###############################################################################
###############################################################################
###############################################################################
if __name__ == '__main__':
    desc = "advent of code - Day 4 - Input MUST BE Sorted"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--file', '-f',
                        help="use file for data instead of STDIN")

    args = parser.parse_args()

    if args.file:
        input_files = [args.file, ]
    else:
        input_files = ['-', ]

    do_work(input_files)
