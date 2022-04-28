'''
- File Name: usecsv.py
- Writer: Geunyoung kim
- Update Information: [2022, 04, 28] File Version 1.0
'''

import csv, re

# read funtion
def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []

    for item in reader:
        output.append(item)

    f.close()
    return output

# write funtion
def writecsv(filename, the_list):
    with open(filename, 'w', newline = '') as f:
        a = csv.writer(f, delimiter = ',')
        a.writerows(the_list)

# Change(Number: char -> float) function
def switch(listname):
    for i in listname:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',', '', j))
            except:
                pass
    return listname