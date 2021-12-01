import utils

data = utils.read_file("./input.txt")


def get_sum(measures, index):
    try:
        return measures[index] + measures[index + 1] + measures[index + 2]
    except IndexError:
        return 0


def compare_windows(measures, index):
    return get_sum(measures, index) < get_sum(measures, index + 1)


def count(measures):
    count = 0

    for index, measure in enumerate(measures):
        if compare_windows(measures, index):
            count += 1

    return count


print(count(data))
