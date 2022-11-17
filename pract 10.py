import mysql.connector as m
conn=m.connect(host='localhost',user='root',database='school')
cur=conn.cursor()
cur.execute('select subject,code from exam where practical=30;')
data=cur.fetchall()
print('CODE\tSUBJECT')
for row in data:
    s,c=row
    print(c,s,sep='\t')
conn.close()
