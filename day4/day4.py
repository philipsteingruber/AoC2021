def part1(numbers, bingo_boards):
    called_numbers = 0
    for number in numbers:
        called_numbers += 1
        for i, bingo_board in enumerate(bingo_boards):
            bingo_boards[i] = mark_number(bingo_board, number)
        if called_numbers >= 5:  # Impossible to win on the first 4 numbers, since all lines are 5 numbers long
            for bingo_board in bingo_boards:
                winning_line_or_none = winning_line(bingo_board)
                if winning_line_or_none:
                    return sum(unmarked_numbers(bingo_board)) * number


def unmarked_numbers(bingo_board):
    unmarked_numbers_list = []
    for line in bingo_board:
        unmarked_numbers_list.extend([x[0] for x in line if x[1] is False])
    return unmarked_numbers_list


def mark_number(bingo_board, number):
    bingo_board_copy = bingo_board.copy()
    for row in bingo_board_copy:
        for i, column in enumerate(row):
            if column[0] == number:
                row[i] = (column[0], True)
                return bingo_board_copy
    return bingo_board_copy


def part2(numbers, bingo_boards):
    bingo_boards_copy = bingo_boards.copy()
    for number in numbers:
        for i, bingo_board in enumerate(bingo_boards_copy):
            bingo_boards[i] = mark_number(bingo_board, number)
        for bingo_board in bingo_boards_copy:
            winning_line_or_none = winning_line(bingo_board)
            if winning_line_or_none:
                if len(bingo_boards_copy) == 1:
                    return sum(unmarked_numbers(bingo_boards_copy[0])) * number
                bingo_boards_copy.remove(bingo_board)


def winning_line(bingo_board):
    for row in bingo_board:
        marked_numbers = [number for number, checked in row if checked]
        if len(marked_numbers) == 5:
            return row
    columns = []
    for i in range(len(bingo_board)):
        columns.append([row[i] for row in bingo_board])
    for column in columns:
        marked_numbers = [number for number, checked in column if checked]
        if len(marked_numbers) == 5:
            return column
    return None


if __name__ == '__main__':
    bingo_boards = []
    current_board = []

    with open('input.txt') as file:
        numbers = list(map(int, file.readline().split(',')))

        for line in file.readlines():
            line = line.strip()
            if len(line.split()) == 5:
                line_numbers = list(map(int, line.split()))
                bingo_line = [(x, False) for x in line_numbers]
                current_board.append(bingo_line)
            if len(current_board) == 5:
                bingo_boards.append(current_board)
                current_board = []
            line = file.readline().strip()

    print('Part 1:', part1(numbers, bingo_boards))
    print('Part 2:', part2(numbers, bingo_boards))

