#Read column file to a dict variable
def fcol2dict(datafile):
    data = {}
    i = 0
    for input in datafile:
        data[i] = input.strip()
        i += 1
    return data

def fcol2list(datafile):
    data = []
    i = 0
    for input in datafile:
        data.append(input.strip())
        i += 1
    return data