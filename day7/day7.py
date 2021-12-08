import math


def part1(crabs):
    best_fuel_used = float('inf')
    for i in range(min(crabs), max(crabs)+1):
        fuel_used = sum([math.fabs(i-crab_pos) for crab_pos in crabs])
        best_fuel_used = min(best_fuel_used, fuel_used)
    return int(best_fuel_used)


def part2(crabs):
    best_fuel_used = float('inf')
    for i in range(min(crabs), max(crabs)+1):
        fuel_used = sum([calculate_fuel_usage(math.fabs(i-crab_pos)) for crab_pos in crabs])
        best_fuel_used = min(best_fuel_used, fuel_used)
    return int(best_fuel_used)


def calculate_fuel_usage(distance):
    return sum(range(1, int(distance)+1))


if __name__ == '__main__':
    with open('input.txt') as file:
        input_data = list(map(int, file.read().split(',')))

    print('Part 1:', part1(input_data))
    print('Part 2:', part2(input_data))
