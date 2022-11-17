file=open('rhyme.txt','w')
file.write('''Would it be ok if I took some of your time?
Would it be ok I wrote you a rhyme?''')
file.close()
file=open('rhyme.txt')
lines=file.readlines()
for line in lines:
    words=line.split()
    for word in words:
        print(word+'#',end='')
    print()
file.close()
