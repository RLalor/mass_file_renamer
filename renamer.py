# simply renames files so you don't have to do it manually to a whole directory

import os
path = '/home/user/directory/anotherDirectory/'
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join(['c' + str(index), '.jpg'])))
