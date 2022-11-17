import mysql.connector as m
mycon=m.connect(host='localhost',user='root')
mycur=mycon.cursor()
mycur.execute('create database school;')
mycur.execute('use school')
mycur.execute("create table student(id int,name char(10),gender char,srank int);")
for i in range(3):
    id=int(input('Student id'))
    name=input('Name')
    gender=input('Gender')
    rank=int(input('Rank'))
    mycur.execute(f"insert into student values({id},'{name}','{gender}',{rank})")
mycon.commit()
mycur.execute('select * from student')
for x in mycur:
    print(x)
mycur.close()
