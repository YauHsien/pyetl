import helpers

def gen_rec(file, help_func):
    fo = open(file, 'r')
    hdr = helpers.header(data= fo.__next__(), help_func= help_func)
    yield hdr
    for l in fo:
        ln = helpers.line(data= l, header= hdr, help_func= help_func)
        yield ln
