import sqns_access.helpers as helpers
import csv
import time

# fo: file object open with read mode
def gen_rec(fo, help_func):
    rt, hdr = helpers.header(data= fo.__next__(), help_func= help_func)
    if rt == 'record':
        yield 'record', hdr
        hdr = hdr['header']
    for _, buf in enumerate(get_line(fo)):
        r = lambda i: helpers.record(data= buf[i], header= hdr,
                                     help_func= help_func)
        yield list(map(r, buf))
        buf = None

def get_line(fo):
    MaxBufSize, buf = 1000000, {}
    for i, line in enumerate(fo):
        buf[i] = line
        if len(buf) == MaxBufSize:
            yield buf
            buf = {}

def test():
    fo = open('../wavein/TWM/ctp_mapping_table_raw.txt', 'r')
    t = time.time()
    for i, x in enumerate(gen_rec(fo, csv.simple_csv)):
        print(time.time() - t)
        t = time.time()
    fo.close()

def test2():
    fo = open('../wavein/TWM/ctp_mapping_table_raw.txt', 'r')
    t = time.time()
    x = fo.readlines()
    print(time.time() - t)
    fo.close()
    for i, line in enumerate(x):
        print(line)
        if i > 8:
            break
