import csv

import os
# from os import open

# homedir = os.getcwd()
csvFile = open("./downloaded/sites/default/files/test.csv", 'w+', newline='')

# csvFile = open(homedir+"/downloaded/sites/default/files/test.csv", 'w+', newline='')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow( (i, i+2, i*2))
finally:
    csvFile.close()
