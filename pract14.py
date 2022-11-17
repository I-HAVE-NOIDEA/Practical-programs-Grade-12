import pickle
bfile=open('student.dat','wb')
print('Enter the no and name of the 5 students:')
for i in range(1,6):
    print('Student',i)
    rno=int(input('Enter roll number:'))
    nm=input('Enter name:')
    bdata=[rno,nm]
    pickle.dump(bdata,bfile)
bfile.close()
choice='y'
while choice.lower()=='y':
    found=False
    rn=int(input('\nEnter the roll no to be searched:'))
    try:
        bfile=open('student.dat','rb')
        while True:
            stu=pickle.load(bfile)
            if stu[0]==rn:
                found=True
                print('Roll No',rn,'is',stu[1])
                break
    except:
        pass
    if found==False:
        print('No student with roll number',rn)
    choice=input('\nDo you want to search more?(y/n):')
