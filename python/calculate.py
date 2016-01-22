# Calculate the m=1x2x3x4x5x...xn, n is input by user

m=1
n=int(input('Please input n number?'))
for i in range (1,n+1):
 m=m*i
 if i==n:
  print(str(i),end='')
 else:
  print(str(i)+'*',end='')
print('=',str(m))
 
