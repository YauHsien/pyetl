# pyetl 資料處理工具組
- 開創日起： 2016/7/2
- 重整日起： 2021/6/15

ETL toolchain in Python.

緣起：由於早些年，我曾有關於資料 ETL 以及許多操作 CSV 的經驗，當時帶著一點想法，開始製作一點點通用的 CSV 模組。 CSV 處理的最主要困難，是當你拿著一個分隔符號去解檔案時，有時遇到的 CSV 檔案是就差那麼一點點，也許某一欄的內容恰好包括了同一個分隔符號，也就是用逗號分隔的 CSV 檔案，某一欄的內容也包含了一些逗號；也就是說，當你解過一個 CSV 檔案時，或許使得在程式的資料變數裡已經包含了一些內容，並或許已經將解過的資料逐行列印在畫面上，但是，對於整個 CSV 資料集，你沒有充足的解析資訊：也許某一行解出的欄位，不知為何少了二個欄位，但總之你不在第一時間發現到那個小錯誤，而後來要經過一番苦工，才發現問題並追蹤到 CSV 檔案裡的瑕疵或細節。

##### 重新整理
目標
- 裁汰 `requirements.txt` 內含的不適用的 Python 程式庫。
- 區隔執行環境：以 [Pipenv](https://docs.python-guide.org/dev/virtualenvs/#:~:text=virtualenv%20is%20a%20tool%20to,standalone%2C%20in%20place%20of%20Pipenv.) 達成。
- 整理 `make` 指令。
- 定位 Python 版本。

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

## 操作方式

- 初次安裝
  ```
  $ make init
  ```
  包含
  - 初次安裝 `pipenv` 到 `./.local/` 路徑。
