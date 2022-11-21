def isEmpty(S):
    if len(S)==0:
        return True
def PUSH(S,item):
    S.append(item)
    top=len(S)-1
def POP(S):
    if isEmpty(S):
        return 'Underflow'
    else:
        val=S.pop()
        return val
def PEEK(S):
    if isEmpty(S):
        return 'Underflow occurs'
    else:
        top=len(S)-1
        return S[top]
    
def SHOW(S):
    if isEmpty(S):
        print('No names found')
    else:
        for i in S[::-1]:
            print(i)
S=[]
while True:
    print('******STACK IMPLEMENTATION USING LIST******')
    print('1:PUSH')
    print('2:POP')
    print('3:PEEK')
    print('4:SHOW')
    print('0:Exit')
    ch=int(input('Enter your choice:'))
    if ch==1:
        val=input('Enter name to insert:')
        PUSH(S,val)
    elif ch==2:
        val=POP(S)
        if val=='Underflow':
            print('Stack is empty!!!')
        else:
            print('Deleted name is:',val)
    elif ch==3:
        val=PEEK(S)
        if val=='Underflow occurs':
            print('Stack is empty')
        else:
            print('Top name is:',val)
    elif ch==4:
        SHOW(S)
    elif ch==0:
        print('Bye')
        break
