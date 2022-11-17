import csv
file=open('books.csv')
print('The details of books costing less than 1000 are displayed below:\n')
reader=csv.reader(file)

try:
    for row in reader:
        if int(row[3])<1000:
            print(row[i],'written by',row[2],'has ID',row[0],'and Price',row[3])
except:
    pass
