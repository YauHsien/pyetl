def split(data, sep):
    array = {'size': 0}
    data1 = data.strip()
    if data1 == '':
        return array
    for i, x in enumerate(data1.split(sep)):
        array[i] = x
    array['size'] = i + 1
    return array

# return: {'size': n+1, 0: v0, 1: v1, ..., n: vn}
def simple_csv(data):
    return split(data, ',')


