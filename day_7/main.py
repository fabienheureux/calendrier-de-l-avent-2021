import utils
import math
from statistics import median, mean

input = utils.read_file("./input")
test_input = utils.read_file("./test_input")


def compute_part_1(data):
    least_fuel_value = median(data)
    return sum([abs(least_fuel_value - value) for value in data])

def get_fuel_comsumption(distance):
    fuel_consumption = [0]

    while distance:
        distance -= 1
        fuel_consumption.append(fuel_consumption[-1] + 1)

    return sum(fuel_consumption)


def compute_part_2(data):
    least_fuel_value = math.floor(mean(data))
    return sum([get_fuel_comsumption(abs(least_fuel_value - value)) for value in data])


print("Part 1 : {}".format(compute_part_1(test_input)))
print("Part 1 : {}".format(compute_part_1(input)))
print("Part 2 : {}".format(compute_part_2(test_input)))
print("Part 2 : {}".format(compute_part_2(input)))
