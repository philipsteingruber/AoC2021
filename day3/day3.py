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


def oxygen_generator(input_data):
    possible_values = input_data.copy()

    for index in range(len(input_data[0])):
        digits_in_order = []
        for inner_index in range(len(input_data[0])):
            digits_in_order.append(''.join([x[inner_index] for x in possible_values]))

        counter = Counter(digits_in_order[index])
        if counter.most_common(2)[0][1] == counter.most_common(2)[1][1]:
            most_common_digit = '1'
        else:
            most_common_digit = counter.most_common(1)[0][0]
        possible_values = [x for x in possible_values if x[index] == most_common_digit]
        if len(possible_values) == 1:
            break

    return int(possible_values[0], 2)


def co2_scrubber(input_data):
    possible_values = input_data.copy()

    for index in range(len(input_data[0])):
        digits_in_order = []
        for inner_index in range(len(input_data[0])):
            digits_in_order.append(''.join([x[inner_index] for x in possible_values]))

        counter = Counter(digits_in_order[index])
        if counter.most_common(2)[0][1] == counter.most_common(2)[1][1]:
            least_common_digit = '0'
        else:
            least_common_digit = counter.most_common(2)[1][0]
        possible_values = [x for x in possible_values if x[index] == least_common_digit]
        if len(possible_values) == 1:
            break

    return int(possible_values[0], 2)


def part2(input_data):
    return oxygen_generator(input_data) * co2_scrubber(input_data)


if __name__ == '__main__':
    with open('input.txt') as file:
        input_data = list(map(str.strip, file.readlines()))

    print('Part 1:', part1(input_data))
    print('Part 2:', part2(input_data))
