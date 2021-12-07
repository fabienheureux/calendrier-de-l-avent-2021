import utils

input = utils.read_file("./input")
test_input = utils.read_file("./test_input")

first_day = 1


def compute(data, days):
    timers = [0] * 9

    for n in data:
        timers[n] += 1

    while days:
        timer_of_the_day = timers.pop(0)
        timers.append(timer_of_the_day)
        timers[6] += timer_of_the_day
        days -= 1

    return sum(timers)


print("Part 1 | test 18 days : {}".format(compute(test_input, 18)))
print("Part 1 | test 80 days : {}".format(compute(test_input, 80)))

print("Part 2 | test 256 days : {}".format(compute(test_input, 256)))
print("Part 2 | input 256 days : {}".format(compute(input, 256)))
