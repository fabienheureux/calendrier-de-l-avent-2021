import utils

data = utils.read_file("./input")
test_data = utils.read_file("./test_input")

def calculate_part_1(data):
    gamma = ""
    epsilon = ""
    for index in range(0, len(data[0]) - 1):
        column = [row[index] for row in data]

        gamma += max(set(column), key=column.count)
        epsilon += min(set(column), key=column.count)

    return int(epsilon, 2) * int(gamma, 2)


print("Part 1: {}".format(calculate_part_1(test_data)))
print("Part 1: {} \n".format(calculate_part_1(data)))
# print("Part 2: {}".format(calculate_part_2(test_data)))
# print("Part 2: {}".format(calculate_part_2(data)))
