#!/bin/bash

python3 fetch_oreilly.py

# 並行的に書籍をダウンロード
python3 print_ids.py | parallel python3 safaribooks.py {}

