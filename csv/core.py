def split(data, sep):
    array = {}
    i = 0
    for x in data.split(sep):
        array[i] = x
        i = i + 1
    array['size'] = i
    return array

# return: {'size': n+1, 0: v0, 1: v1, ..., n: vn}
def simple_csv(data):
    return split(data, ',')


