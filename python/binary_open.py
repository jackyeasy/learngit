def is_gif(fname):
 f=open(fname,'br')
 first4=tuple(f.read(4))
 return first4 == (0x47,0x49,0x46,0x38)


name='mesg'
if is_gif(name):
 print(name+"is a gif file")
else:
 print(name+"is not a gif file")


