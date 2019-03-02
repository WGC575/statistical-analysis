def readData(datafile):
    data = {}
    i = 0
    for input in datafile:
        data[i] = input.strip()
        i += 1
    return data
