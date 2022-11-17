import mysql.connector as m
conn=m.connect(host='localhost',user='root',database='school')
cur=conn.cursor()
cur.execute('select subject,code from exam;')
for row in cur:
    s,c=row
    print(s,'(',c,')',sep='')
conn.close()
