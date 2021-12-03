from collections import Counter


def part1(input_data):
    digits_in_order = []

    for index in range(len(input_data[0])):
        digits_in_order.append(''.join([x[index] for x in input_data]))

    gamma = []
    epsilon = []
    for li in digits_in_order:
        counter = Counter(li)
        most_common = counter.most_common(2)
        gamma.append(most_common[0][0])
        epsilon.append(most_common[1][0])

    gamma = int(''.join(gamma), 2)
    epsilon = int(''.join(epsilon), 2)
    return gamma * epsilon


def part2(input_data):
    pass


if __name__ == '__main__':
    with open('input.txt') as file:
        input_data = list(map(str.strip, file.readlines()))

    print('Part 1:', part1(input_data))
    print('Part 2:', part2(input_data))
