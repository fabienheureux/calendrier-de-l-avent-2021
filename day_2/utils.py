def read_file(path):
    data = []
    with open(path) as f:
        for line in f:
            data.append(line.rstrip().split(" "))

    return data
