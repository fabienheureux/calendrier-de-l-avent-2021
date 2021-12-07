def read_file(path):
    data = []
    with open(path) as f:
        for line in f:
            data.append(line.replace("\n", ""))

    boards = [[]]
    board_index = 0
    order = data[0].split(',')

    for line in data[1:]:
        if len(line) > 0:
            try:
                boards[board_index].append(line)
            except IndexError:
                boards.append([line])
        else:
            board_index += 1

    return order, boards
