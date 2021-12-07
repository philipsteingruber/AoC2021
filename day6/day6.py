import timeit
from collections import defaultdict

def calculate_fish_growth(fish_timers, days):
    days_remaining = days
    buckets = defaultdict(int)

    for fish_timer in fish_timers:
        buckets[fish_timer] += 1

    while days_remaining > 0:
        new_buckets = defaultdict(int)

        for i in range(1, 9):
            new_buckets[i-1] = buckets[i]

        zeroes = buckets[0]
        new_buckets[6] += zeroes
        new_buckets[8] += zeroes

        buckets = new_buckets
        days_remaining -= 1

    return buckets


if __name__ == '__main__':
    with open('input.txt') as file:
        input_data = list(map(int, file.read().split(',')))
    print('Part 1:', sum(calculate_fish_growth(input_data, 80).values()))
    print('Part 2:', sum(calculate_fish_growth(input_data, 256).values()))
