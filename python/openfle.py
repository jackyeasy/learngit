def print_file(fname):
 f=open(fname,"r")
 for line in f:
  print(line, end='')
 f.close()

file="./profile"
#print_file(file)


def print_file2(fname):
 f=open(fname)
 print(f.read())
 f.close()

#print_file2(file)

# even a very simplest one
#print(open(file).read())

llist=open(file).read()
print(llist)





