file='./profile'
f=open(file,'r+')
temp=f.read()
temp='add the first line\n'+temp
f.seek(0)
f.write(temp)
f.close()

