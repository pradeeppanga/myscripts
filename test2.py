#!/usr/bin/python

import datetime

file_list = []

for i in range(0, 6):
    current_date = datetime.datetime.now() - datetime.timedelta(hours=i)
    file_list.append("/data/app/web/logs/TTO" + current_date.strftime("%Y%m%d%H"))

for __file in file_list:
    print __file
print file_list

