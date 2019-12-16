#!/usr/bin/env python3
"""Advent of code."""
#
# https://adventofcode.com/2019
#
import fileinput
import argparse


def _calc_segments(directions):

    # Right = add to X
    # Left = subtract from X
    # Up = add to Y
    # down = subtract from Y

    starting_x = ending_x = 0
    starting_y = ending_y = 0

    route = []

    for pt in directions:
        move = pt[0].upper()
        length = int(pt[1:])
        if move == 'R':
            ending_x += length
            ending_y = starting_y
        elif move == 'L':
            ending_x -= length
            ending_y = starting_y
        elif move == 'U':
            ending_y += length
            ending_x = starting_x
        elif move == 'D':
            ending_y -= length
            ending_x = starting_x
        else:
            assert False
        segment = ((starting_x, starting_y), (ending_x, ending_y))
        starting_x = ending_x
        starting_y = ending_y
        route.append(segment)

    return route


def do_work(files):
    """For the data in the file(s), do the work of solving the puzzle."""

    # for each path, record it's segments (start and end) in a list.
    # For example, [((0,0), (0,1)), ((0,1), (5,1)), ...]
    # then we can compare the segments and find intersections.
    # the distance from the origin is just the addition of x+y
    routes = []

    for i, line in enumerate(fileinput.input(files=files)):
        data = line[:-1].split(',')
        routes.append(_calc_segments(data))

    # print(routes)
    # find the intersections
    # if x1 const (vertical line)
    #  x2start <= x1 <= x2end
    # and if y2 const (horizontal line)
    #   y1start <= y2 <= y1end
    # then
    #   they intersect a2 (x1, y2)
    #   unless the point is (0, 0), then we skip it
    distance = 0xFFFFFFFF
    for segment_1 in routes[0]:
        horizontal = False
        vertical = False
        # print('*' * 80)
        (start_x_1, start_y_1), (end_x_1, end_y_1) = segment_1
        # we want the segments to go up or to the right, so swap
        # the positions if they're down or left
        if end_x_1 < start_x_1 or end_y_1 < start_y_1:
            temp = start_x_1
            start_x_1 = end_x_1
            end_x_1 = temp

            temp = start_y_1
            start_y_1 = end_y_1
            end_y_1 = temp

        # find the vertical line
        if start_x_1 == end_x_1:
            vertical = True

        # find a horizontal line
        elif start_y_1 == end_y_1:
            horizontal = True

        # something is wrong?
        else:
            assert False
        for segment_2 in routes[1]:

            if (0, 0) in segment_2 and (0, 0) in segment_1:
                continue

            (start_x_2, start_y_2), (end_x_2, end_y_2) = segment_2

            # we want the segments to go up or to the right, so swap
            # the positions if they're down or left
            if end_x_2 < start_x_2 or end_y_2 < start_y_2:
                temp = start_x_2
                start_x_2 = end_x_2
                end_x_2 = temp

                temp = start_y_2
                start_y_2 = end_y_2
                end_y_2 = temp

            if start_x_2 == end_x_2:
                if vertical:  # 2 vertical lines don't intersect
                    continue
                if start_x_1 <= start_x_2 <= end_x_1 \
                        and start_y_2 <= start_y_1 <= end_y_2:
                    if distance > abs(start_x_2) + abs(start_y_1):
                        distance = abs(start_x_2) + abs(start_y_1)

            # find a horizontal line
            elif start_y_2 == end_y_2:
                if horizontal:
                    continue  # 2 horizontal lines don't intersect

                if start_x_2 <= start_x_1 <= end_x_2 \
                        and start_y_1 <= start_y_2 <= end_y_1:
                    if distance > abs(start_y_2) + abs(start_x_1):
                        distance = abs(start_y_2) + abs(start_x_1)

            # something is wrong?
            else:
                assert False

    print("distance: {}".format(distance))


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
