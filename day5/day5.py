import re
from collections import defaultdict
import math


def part1(input_data):
    max_width = -1
    max_height = -1

    for line in input_data:
        x1, y1, x2, y2 = line
        max_width = max(max_width, x1)
        max_width = max(max_width, x2)
        max_height = max(max_height, y1)
        max_height = max(max_height, y2)

    coordinates = defaultdict(int)

    for x1, y1, x2, y2 in input_data:
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                coordinates[(x, y1)] += 1
        elif x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                coordinates[(x1, y)] += 1

    return len([x for x in coordinates.keys() if coordinates[x] > 1])


def part2(input_data):
    coordinates = defaultdict(int)

    for x1, y1, x2, y2 in input_data:
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                point = x, y1
                coordinates[point] += 1
        elif x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                point = x1, y
                coordinates[point] += 1
        elif math.fabs(x1 - x2) == math.fabs(y1 - y2):
            if x1 > x2 and y1 > y2:
                for x in range(x2, x1+1):
                    point = x, y2+(x-x2)
                    coordinates[point] += 1
            elif x1 > x2 and y1 < y2:
                for x in range(x2, x1+1):
                    point = x, y2-(x-x2)
                    coordinates[point] += 1
            elif x1 < x2 and y1 > y2:
                for x in range(x1, x2+1):
                    point = x, y1-(x-x1)
                    coordinates[point] += 1
            elif x1 < x2 and y1 < y2:
                for x in range(x1, x2+1):
                    point = x, y1+(x-x1)
                    coordinates[point] += 1
    return len([x for x in coordinates.keys() if coordinates[x] > 1])


def display_map(coordinates, max_height, max_width):
    for y in range(max_height+1):
        row = []
        for x in range(max_width+1):
            coord = coordinates[x, y]
            if coord == 0:
                coord = '.'
            row.append(str(coord))
        print(''.join(row))


if __name__ == '__main__':
    pattern = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')

    with open('input.txt') as file:
        input_data = [list(map(int, re.match(pattern, x).groups())) for x in map(str.strip, file.readlines())]

    print('Part 1:', part1(input_data))
    print('Part 2:', part2(input_data))
