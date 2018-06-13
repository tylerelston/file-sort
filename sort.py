#todo: assertions
import os
while True:
    try:
        directory = input('Directory: ')
        assert (os.path.isdir(directory) == True), 'dir does not exist'
        #assert os.access('test',os.F_OK), 'No access'
    except AssertionError as e:
        print('Error: ',e)
        continue
    break

files = {}
for f in os.listdir(directory):
    if os.path.isfile(os.path.join(directory,f)):
        ext = f.split('.')[1]
        if ext not in files:
            files[ext] = [f]
        else:
            files[ext].append(f)
            
if not os.path.exists(os.path.join(directory,'Sorted')):
    os.mkdir(os.path.join(directory,'Sorted'))
    
d = os.path.join(directory,'Sorted')
for e in files:
    if not os.path.exists(os.path.join(d,e)):
        os.mkdir(os.path.join(d,e))
    for f in files[e]:
        os.rename(os.path.join(directory,f),os.path.join(d,e,f))

print('Sorted!')
