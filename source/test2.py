#!/usr/bin/python

import datetime
from subprocess import call

file_list = []

for i in range(0, 6):
    current_date = datetime.datetime.now() - datetime.timedelta(hours=i)
    file_list.append("/data/" + current_date.strftime("%Y%m%d%H"))

for __file in file_list:
    print __file
    call(["hdfs", "dfs", "-stat", __file])
print file_list

