'''
- File Name: csv_function.py
- Writer: Geunyoung kim
- Update Information: [2022, 04, 28] File Version 1.0
'''

import usecsv, re

# Make a file of information of Apartment
def make_file(local, extent, price):
    total = usecsv.opencsv('apt_201910.csv')
    newapt = usecsv.switch(total)

    new = []
    for i in newapt:
        try:
            if re.match(local, i[0]) and i[5] >= extent and i[-4] <= price:
                new.append([i[0], i[4], i[-4]])
        except:
            pass

    usecsv.writecsv('newapt.csv', new)