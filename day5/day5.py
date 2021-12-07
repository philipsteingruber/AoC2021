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

    # display_map(coordinates, max_height, max_width)
    return len([x for x in coordinates.keys() if coordinates[x] > 1])


def part2(input_data):
    max_width = -1
    max_height = -1

    for line in input_data:
        x1, y1, x2, y2 = line
        max_width = max(max_width, x1)
        max_width = max(max_width, x2)
        max_height = max(max_height, y1)
        max_height = max(max_height, y2)

    coordinates = defaultdict(int)

    handled_lines = 0
    for x1, y1, x2, y2 in input_data:
        # print(x1, ',', y1, ' -> ', x2, ',', y2, sep='')
        if y1 == y2:
            # 2,5 -> 4,5 = (2,5), (3,5), (4,5)
            handled_lines += 1
            added_points = 0
            for x in range(min(x1, x2), max(x1, x2) + 1):
                added_points += 1
                point = x, y1
                coordinates[point] += 1
                # print('1 Adding 1 to point', point, '. New value:', coordinates[point])
            if added_points != math.fabs(x1-x2) + 1:
                print('WRONG 1')
        elif x1 == x2:
            # 4,5 -> 4,8 = (4,5), (4,6), (4,7), (4,8)
            handled_lines += 1
            added_points = 0
            for y in range(min(y1, y2), max(y1, y2) + 1):
                added_points += 1
                point = x1, y
                coordinates[point] += 1
                # print('2 Adding 1 to point', point, '. New value:', coordinates[point])
            if added_points != math.fabs(y1-y2) +1:
                print('WRONG 2')
        elif math.fabs(x1 - x2) == math.fabs(y1 - y2):
            if x1 > x2 and y1 > y2:
                # 6,4 -> 2,0 = (6,4), (5,3), (4,2), (3,1), (2,0)
                handled_lines += 1
                added_points = 0
                for x in range(x2, x1+1):
                    added_points += 1
                    point = x, y2+(x-x2)
                    coordinates[point] += 1
                    # print('3 Adding 1 to point', point, '. New value:', coordinates[point])
                if added_points != math.fabs(x1-x2) + 1:
                    print('WRONG 3')
            elif x1 > x2 and y1 < y2:
                # 6,0 -> 2,4 = (6,0), (5,1), (4,2), (3,3), (2,4)
                handled_lines += 1
                added_points = 0
                for x in range(x2, x1+1):
                    added_points += 1
                    point = x, y2-(x-x2)
                    coordinates[point] += 1
                    # print('4 Adding 1 to point', point, '. New value:', coordinates[point])
                if added_points != math.fabs(x1-x2) + 1:
                    print('WRONG 4')
            elif x1 < x2 and y1 > y2:
                # 5,5 -> 8,2 = (5,5), (6,4), (7,3), (8,2)
                # 0,3 -> 3,0 = (0,3), (1,2), (2,1), (3,0)
                handled_lines += 1
                added_points = 0
                for x in range(x1, x2+1):
                    added_points += 1
                    point = x, y1-(x-x1)
                    coordinates[point] += 1
                    # print('5 Adding 1 to point', point, '. New value:', coordinates[point])
                if added_points != math.fabs(x1-x2) + 1:
                    print('WRONG 5')
            elif x1 < x2 and y1 < y2:
                # 5,2 -> 8,5 = (5,2), (6,3), (7,4), (8,5)
                handled_lines += 1
                added_points = 0
                for x in range(x1, x2+1):
                    added_points += 1
                    point = x, y1+(x-x1)
                    coordinates[point] += 1
                    # print('6 Adding 1 to point', point, '. New value:', coordinates[point])
                if added_points != math.fabs(x1-x2) + 1:
                    print('WRONG 6')
            else:
                print('Skipped line:', x1, y1, x2, y2)
        else:
            print('Skipped line:', x1, y1, x2, y2)
        # display_map(coordinates, max_height, max_width)
        # print('\n')
    # display_map(coordinates, max_height, max_width)
    # print(coordinates.items())
    if handled_lines != len(input_data):
        print('WRONG')
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
