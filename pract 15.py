import pickle
bfile=open('marks.dat','wb')
print('Enter the no,name and marks of the 5 students:')
for i in range(1,6):
    print('Student',i)
    rno=int(input('Enter roll number:'))
    nm=input('Enter name:')
    mks=int(input('Enter marks(out of 500):'))
    bdata=[rno,nm,mks]
    pickle.dump(bdata,bfile)
bfile.close()
choice='y'
while choice.lower()=='y':
    found=False
    rn=int(input('\nEnter no of student whose marks are to be updated:'))
    try:
        bfile=open('marks.dat','rb+')
        while True:
            pos=bfile.tell()
            stu=pickle.load(bfile)
            if stu[0]==rn:
                found=True
                stu[2]=int(input('Enter new marks:'))
                bfile.seek(pos)
                pickle.dump(stu,bfile)
                bfile.flush()
                break
    except:
        pass
    if found==False:
        print('No student with roll number',rn)
    choice=input('\nDo you want to update more?(y/n):')
    bfile.seek(0)
print('The contents of\'marks.dat\' are as follows:')
try:
    while True:
        stu=pickle.load(bfile)
        print(stu)
except:
    pass
