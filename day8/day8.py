import re


def part1(input_data):
    occurences = 0
    for line in input_data:
        outputs = line[1]
        occurences += len([x for x in outputs if len(x) in [2, 3, 4, 7]])
    return occurences


def part2(input_data):
    digits = {'acedgfb': 8,
              'cdfbe': 5,
              'gcdfa': 2,
              'fbcad': 3,
              'dab': 7,
              'cefabd': 9,
              'cdfgeb': 6,
              'eafb': 4,
              'cagedb': 0,
              'ab': 1}

    total = 0
    for line in input_data:
        output_digits = []
        for output in line[1]:
            for digit in digits:
                if sorted(output) == sorted(digit):
                    output_digits.append(digits[digit])
        print(output_digits)

        try:
            total += int(''.join([str(x) for x in output_digits]))
        except ValueError:
            print(output_digits)
    return total





if __name__ == '__main__':
    pattern = re.compile(r'([a-g ]+) | ([a-g ]+)')
    input_data = []
    with open('input.txt') as file:
        for line in file.readlines():
            input_data.append([x.split() for x in line.strip().split(' | ')])

    print('Part 1:', part1(input_data))
    print('Part 2:', part2(input_data))
