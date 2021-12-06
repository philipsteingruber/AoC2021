import re
from collections import defaultdict

def part1(input_data):
    max_width = -1
    max_height = -1

    for line in input_data:
        x1, y1, x2, y2 = line
        max_width = max(max_width, x1)
        max_width = max(max_width, x2)
        max_height = max(max_height, y1)
        max_height = max(max_height, y2)

    # map = [[0] * max_width] * max_height
    map = defaultdict(int)

    for x1, y1, x2, y2 in input_data:
        print(x1, y1, x2, y2)
        if x1 != x2:
            for x in range(min(x1, x2), max(x1, x2)):
                map[(x, y1)] += 1
                print('Adding 1 to point', (x, y1), '. New value:', map[x, y1])
        elif y1 != y2:
            for y in range(min(y1, y2), max(y1, y2)):
                map[(x1, y)] += 1
                print('Adding 1 to point', (x1, y), '. New value:', map[x1, y])

    print(dict(map))
    return len([x for x in map.keys() if map[x] > 1])

def part2(input_data):
    pass


if __name__ == '__main__':
    pattern = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')

    with open('input.txt') as file:
        input_data = [list(map(int, re.match(pattern, x).groups())) for x in file.readlines()]

    print('Part 1', part1(input_data))
    print('Part 2', part2(input_data))
