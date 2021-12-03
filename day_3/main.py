import utils

data = utils.read_file("./input")
test_data = utils.read_file("./test_input")


def get_column(data, index):
    return [row[index] for row in data]


def calculate_part_1(data):
    gamma = ""
    epsilon = ""
    for index in range(0, len(data[0]) - 1):
        column = get_column(data, index)

        gamma += max(set(column), key=column.count)
        epsilon += min(set(column), key=column.count)

    return int(epsilon, 2) * int(gamma, 2)


def get_rating(columns, data, bit_criteria, comparison_function, index=0):
    initial_bit_criteria = bit_criteria

    if len(data) > 1:
        column = get_column(data, index)

        if min(set(column), key=column.count) != max(set(column), key=column.count):
            bit_criteria = int(comparison_function(set(column), key=column.count))

        filtered_data = [row for row in data if int(row[index]) == bit_criteria]

        return get_rating(index, filtered_data, initial_bit_criteria, comparison_function, index + 1)
    else:
        return int(data[0], 2)


def calculate_part_2(data):
    columns = []

    for index in range(0, len(data[0]) - 1):
        columns.append([row[index] for row in data])

    oxygen_generator_rating = get_rating(columns, data, 1, max)
    co2_scrubber_rating = get_rating(columns, data, 0, min)

    return oxygen_generator_rating * co2_scrubber_rating


print("Part 1: {}".format(calculate_part_1(test_data)))
print("Part 1: {} \n".format(calculate_part_1(data)))
print("Part 2: {}".format(calculate_part_2(test_data)))
print("Part 2: {}".format(calculate_part_2(data)))
