import utils

order, boards = utils.read_file("./input")
order, boards = utils.read_file("./test_input")


# def check_presence(number, board):

def get_columns(rows):
    if len(rows) == 0:
        return []

    row_length = len(rows[0].split())
    col_length = len(rows)

    columns = []
    for col_index in range(0, row_length):
        columns.append([rows[row_index].split()[col_index] for row_index in range(0, col_length)])

    return columns

def get_rows(board):
    return [row.lstrip().rstrip() for row in board]

def calculate_part_1(order, boards):
    for number in order:
        for board in boards:
            rows = get_rows(board, number)
            columns = get_columns(rows, number)

            for row in rows:
                return [item for item in row if item != number]

            for col in columns:
                return [item for item in col if item != number]



print("Part 1 | test : {}".format(calculate_part_1(order, boards)))
# print("Part 1: {} \n".format(calculate_part_1()))
# print("Part 2: {}".format(calculate_part_2(test_data)))
# print("Part 2: {}".format(calculate_part_2(data)))
