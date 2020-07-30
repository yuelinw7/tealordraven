import csv
import os
import re

with open ('./pdf_list.txt','r') as f:
    lines=f.readlines()
    cnt = 0
    for line in lines:
        cnt += 1
        os.system('wget -4 --tries=1 --timeout=3 --output-file=./log/logfile' + str(cnt) + ' --delete-after ' + line)

