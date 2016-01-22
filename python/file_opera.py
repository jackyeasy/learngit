import os
def list_cwd():
 return os.listdir(os.getcwd())

for p in list_cwd():
 if os.path.isfile(p):print(p) 

print("above are files")

for q in list_cwd():
 if os.path.isdir(q): print(q)
