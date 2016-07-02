# pyetl
ETL toolchain in Python.

### Toolchain

#### Sequential Access on File

By using `sqns_access` module, processing of a sequential access file can be effecient, flexible, and easy to access and validate each record in the file.

`sqns_access.gen_rec(fo, help_func)`: to read a `file` and process it with `help_func`.

`sqns_access.helpers.header(data, help_func)`: to process `data` with `help_func`, then return a `header`.

`sqns_access.helpers.line(data, header, help_func)`: to process `data` with `help_func`, then return a `line`.

`help_func` may be `csv.simple_csv` or `csv.helpers.simple_ssv`.

#### Comma-or-other Separated Values

To convert data into CSV, or SSV, Semi-colon Separated Values.

`csv.simple_csv(data)`: to get a CSV version of data.

`csv.helpers.simple_ssv(data)`: to get a SSV version of data.
