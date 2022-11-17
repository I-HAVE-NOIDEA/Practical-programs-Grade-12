import mysql.connector as m
mycon=m.connect(host='localhost',user='root',database='school')
mycur=mycon.cursor()
rollno=int(input('Enter rollno to search'))
mycur.execute(f"select * from student where id={rollno}")
x=mycur.fetchone()
if x==None:
    print('Not a valid Rollno')
else:
    print('details')
    print('Id-',x[0],'name-',x[1],'gender-',x[2],'rank-',x[3])
    rank=int(input('Enter rank to update'))
    mycur.execute(f"update student set srank={rank} where id ={rollno}")
    mycon.commit()
    print('After updation..Student table')
    mycur.execute('select * from student')
    for x in mycur:
        print(x)
mycur.close()
