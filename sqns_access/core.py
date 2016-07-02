import helpers

# fo: file object open with read mode
def gen_rec(fo, help_func):
    hdr = helpers.header(data= fo.__next__(), help_func= help_func)
    for l in fo:
        ln = helpers.line(data= l, header= hdr, help_func= help_func)
        yield ln
