# For summary

n=int(input('Please input how many number do you want to sum?'))
total=0
for i in range (n):
 s=input('Enter number '+str(i+1)+':')
 total=total+int(s)
print('The total numbers sum is',str(total))

