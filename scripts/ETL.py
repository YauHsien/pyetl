import _io, pathlib, logging

class ETL:

    def __init__(self, header, delimiter= ','):
        if type(header) is dict:
            self.header = header
            self.delimiter = delimiter
            self.fin = None
            self.fout = None
            self.line = None

    def approach(self, infile, outfile):
        if pathlib.Path(infile).is_file() and pathlib.Path(outfile).is_file():
            self.fin = open(str(infile), 'r')
            self.fout = open(str(outfile), 'w')
            
            header = dict()
            for _, ln in iter(self.fin):
                line = ln.rstrip()
                if line == '':
                    break
                for i, term in enumerate(line.split(self.delimiter)):
                    header[i] = term
                break
            
            for _, ln in iter(self.fin):
                line = ln.rstrip()
                if line == '':
                    break
                self._new_line()
                for i, term in enumerate(line.split(self.delimiter)):
                    self._extract(header[i], term)
                self._transform()

            self.fin.close()
            self.fout.close()

    def _new_line(self):
        self.line = dict()
            
    def _extract(self, column, value):
        if type(self.header) is not dict:
            logging.debug('bad header: {} {}'.format(type(self.header), header))
        elif type(self.fin) is not _io.TextIOWrapper:
            logging.debug('bad in-file: {} {}'.format(type(self.fin), fin))
        elif type(self.fout) is not _io.TextIOWrapper:
            logging.debug('bad out-file: {} {}'.format(type(self.fout), fout))
        else:
            if column in self.header:
                self.line[self.header[column]] = value

    def _transform(self):
        if type(self.header) is not dict:
            logging.debug('bad header: {} {}'.format(type(self.header), header))
        elif type(self.fin) is not _io.TextIOWrapper:
            logging.debug('bad in-file: {} {}'.format(type(self.fin), fin))
        elif type(self.fout) is not _io.TextIOWrapper:
            logging.debug('bad out-file: {} {}'.format(type(self.fout), fout))
        else:
            line1 = list()
            for _, key in enumerate(sorted(self.line)):
                line1.add(self.line[key])
            self.fout.write(self.delimiter.join(line1))
