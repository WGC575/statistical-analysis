#Read column file to a dict variable, int
def fcol2dict(datafile):
    data = {}
    i = 0
    for input in datafile:
        data[i] = int(input.strip())
        i += 1
    return data

#Read column file to a list variable, int
def fcol2list(datafile):
    data = []
    i = 0
    for input in datafile:
        data.append(int(input.strip()))
        i += 1
    return data