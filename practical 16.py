import pickle,os
bfile=open('emp.dat','wb')
print('Enter the id,name and salary of the 5 employees:')
for i in range(1,6):
    print('Employee',i)
    empid=int(input('Enter employee id:'))
    empname=input('Enter name:')
    salary=int(input('Enter salary:'))
    bdata=[empid,empname,salary]
    pickle.dump(bdata,bfile)
bfile.close()
try:
    bfile=open('emp.dat','rb')
    tfile=open('temp.dat','wb')
    print()
    while True:
        emp=pickle.load(bfile)
        if emp[2]>25000:
            print('This record will be deleted-->',emp)
        else:
            pickle.dump(emp,tfile)
except:
    pass
tfile.close()
bfile.close()
os.remove('emp.dat')
os.rename('temp.dat','emp.dat')
print("\nThe contents of \'emp.dat\' are as follows:")
try:
    bfile=open('emp.dat','rb')
    while True:
        emp=pickle.load(bfile)
        print(emp)
except:
    pass
bfile.close()
    
