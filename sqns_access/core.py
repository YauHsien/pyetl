import sqns_access.helpers as helpers

# fo: file object open with read mode
def gen_rec(fo, help_func):
    rt, hdr = helpers.header(data= fo.__next__(), help_func= help_func)
    if rt == 'record':
        yield hdr
        hdr = hdr['header']
    for ln in fo:
        rd = helpers.record(data= ln, header= hdr, help_func= help_func)
        yield rd
