import utils

data = utils.read_file("./input.txt")

def count(measures):
    count = 0

    for index, measure in enumerate(measures):
        if index == 0:
            pass

        elif measures[index] > measures[index - 1]:
            count += 1

    return count

print(count(data))
