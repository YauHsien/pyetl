# help_func: some function like csv.simple_csv or csv.helpers.simple_ssv
# return: {'size': n+1, 0: v0, 1: v1, ..., n: vn, v0: 0, v1: 1, ..., vn: n}
def header(data, help_func):
    array = help_func(data)
    for i in range(0, array['size']):
        array[array[i]] = i
    return array

# help_func: some function like csv.simple_csv or csv.helpers.simple_ssv
# return: {'header': hdr, 'size': n+1, 0: v0, 1: v1, ..., n: vn}
def line(data, header, help_func):
    array = help_func(data)
    array['header'] = header
    return array
