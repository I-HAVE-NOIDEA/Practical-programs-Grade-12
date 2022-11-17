import pickle
def add_rec(file):
    bfile=open(file,'ab')
    print('Enter the no and name of the 2 students:')
    for i in range(1,3):
        print('Student',i)
        rno=int(input('Enter roll number:'))
        nm=input('Enter name:')
        bdata=[rno,nm]
        pickle.dump(bdata,bfile)
    print('\n',i,'records added')
    bfile.close()
file_name='student.dat'
add_rec(file_name)
print('\nThe contents of \'student.dat\' is shown below:')
try:
    bfile=open('student.dat','rb')
    while True:
        stu=pickle.load(bfile)
        print(stu)
except:
    pass
bfile.close()
