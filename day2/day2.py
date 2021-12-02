def part1(input_data):
    depth = 0
    horizontal_pos = 0

    for instruction in input_data:
        dir, value = instruction.split(' ')
        value = int(value)
        if dir == 'forward':
            horizontal_pos += value
        elif dir == 'up':
            depth -= value
        elif dir == 'down':
            depth += value

    return depth * horizontal_pos


def part2(input_data):
    depth = 0
    horizontal_pos = 0
    aim = 0

    for instruction in input_data:
        dir, value = instruction.split(' ')
        value = int(value)
        if dir == 'forward':
            horizontal_pos += value
            depth += aim * value
        elif dir == 'down':
            aim += value
        elif dir == 'up':
            aim -= value

    return depth * horizontal_pos


if __name__ == '__main__':
    with open('input.txt') as file:
        input_data = file.readlines()

    print('Part 1:', part1(input_data))
    print('Part 2:', part2(input_data))
