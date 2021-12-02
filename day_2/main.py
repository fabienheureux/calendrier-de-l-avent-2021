import utils

data = utils.read_file("./input")
test_data = utils.read_file("./test_input")


def calculate_part_1(instructions):
    def get_computed_value(move, value):
        if move in ["forward", "down"]:
            return value
        return -1 * value

    horizontal = sum(
        [
            get_computed_value(move, int(value))
            for move, value in data
            if move != "forward"
        ]
    )
    depth = sum(
        [
            get_computed_value(move, int(value))
            for move, value in data
            if move == "forward"
        ]
    )

    return horizontal * depth


def calculate_part_2(instructions):
    aim = 0
    depth = 0
    horizontal = 0

    for move, value in instructions:
        value = int(value)

        if move == "down":
            aim -= value
        if move == "up":
            aim += value
        if move == "forward":
            horizontal += value
            depth += value * aim

    return horizontal * depth


print("Part 1: {}".format(calculate_part_1(test_data)))
print("Part 1: {} \n".format(calculate_part_1(data)))
print("Part 2: {}".format(calculate_part_2(test_data)))
print("Part 2: {}".format(calculate_part_2(data)))
