import sqns_access.helpers as helpers
import _io
import inspect

def gen_rec(fo, help_func):
    if fo.__class__ is _io.TextIOWrapper and \
    inspect.isfunction(help_func) and len(inspect.getargspec(help_func)) == 1:
        rt, hdr = helpers.header(data= fo.__next__(), help_func= help_func)
        if rt == 'record':
            yield hdr
            hdr = hdr['header']
        for ln in fo:
            rd = helpers.record(data= ln, header= hdr, help_func= help_func)
            yield rd
    else:
        raise BadArgError({'fo': fo.__class__,
                           'help_func': help_func.__class__})

class BadArgError(ValueError):
    pass
