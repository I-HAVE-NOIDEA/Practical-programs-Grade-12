import csv
col=['Book ID','Title','Author','Price']
with open('books.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(col)
    choice='y'
    while choice.lower()=='y':
        row=[]
        bkid=int(input('Enter book id:'))
        title=input('Enter title:')
        auth=input('Enter author:')
        price=int(input('Enter price:'))
        row.extend([bkid,title,auth,price])
        writer.writerow(row)
        choice=input('Enter more?(y/n):')
    print('Written successfully!!!')
file=open('books.csv','r')
print('\nThe contents of \'book.csv\' is shown below')
reader=csv.reader(file)
try:
    for row in reader:
        print(row)
except:
    pass
    
