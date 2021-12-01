def part1(input_data):
    return len([x for i, x in enumerate(input_data) if input_data[i-1] < input_data[i]])


def part2(input_data):
    measurements = []

    for index in range(len(input_data)-2):
        measurements.append(sum(input_data[index:index+3]))

    return len([x for i, x in enumerate(measurements) if measurements[i-1] < measurements[i]])


if __name__ == '__main__':
    with open('input.txt') as file:
        input_data = list(map(int, file.readlines()))

    print('Part 1:', part1(input_data))
    print('Part 2:', part2(input_data))
