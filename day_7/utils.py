def read_file(path):
    data = []
    with open(path) as f:
        for line in f:
            for item in line.split(","):
                data.append(int(item))

    return data
