import os
file='class2/test.py'
if os.path.exists(file):
    os.remove(file)
    print('the file has been removed successfully')
else:
    print('the file dose not exist')