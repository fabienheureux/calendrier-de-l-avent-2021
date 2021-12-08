import utils

order, boards = utils.read_file("./input")
order_test, boards_test = utils.read_file("./test_input")

def get_columns(rows):
    if len(rows) == 0:
        return []

    row_length = len(rows[0])
    col_length = len(rows)

    columns = []
    for col_index in range(0, row_length):
        columns.append(
            [rows[row_index][col_index] for row_index in range(0, col_length)]
        )

    return columns


def get_rows(board):
    return [row.split() for row in [row.lstrip().rstrip() for row in board]]


def update_list(list, number):
    if number in list:
        list.remove(number)
    return list

def flatten(t):
    return [int(item) for sublist in t for item in sublist]

def check_bingo(rows, columns, numbers, index=0):
    if [] in rows:
        return (flatten(rows), index)
    elif [] in columns:
        return (flatten(columns), index)
    elif index == len(numbers) - 1:
        return False
    else:
        number = numbers[index]
        new_rows = [update_list(row, number) for row in rows]
        new_columns = [update_list(col, number) for col in columns]
        return check_bingo(new_rows, new_columns, numbers, index + 1)



def calculate_part_1(numbers, boards):
    fastest = len(numbers)
    result = []

    for board in [board for board in boards if len(board) > 0]:
        rows = get_rows(board)
        columns = get_columns(rows)
        score, index = check_bingo(rows, columns, numbers)

        if index < fastest:
            fastest = index
            last_number = numbers[index - 1]
            result = [sum(score), int(last_number)]

    return result[0] * result[1]

def calculate_part_2(numbers, boards):
    longest = 0
    result = []
    for board in [board for board in boards if len(board) > 0]:
        rows = get_rows(board)
        columns = get_columns(rows)
        score, index = check_bingo(rows, columns, numbers)

        if index > longest:
            longest = index
            last_number = numbers[index - 1]
            result = [sum(score), int(last_number)]

    return result[0] * result[1]



print("Part 1 | test : {}".format(calculate_part_1(order_test, boards_test)))
print("Part 1: {} \n".format(calculate_part_1(order, boards)))
print("Part 2 | test: {}".format(calculate_part_2(order_test, boards_test)))
print("Part 2: {}".format(calculate_part_2(order, boards)))
