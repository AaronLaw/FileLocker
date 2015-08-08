''' test shutil.copytree()
2015-08-05, by Aaron Law

cation:
As it uses Robocopy, Windows only
'''

import shutil
import os # os.path.join()

# to handle path on Windows
from pathlib import Path, PurePath

folders=['AA0008', 'AA0025']
# folder='AA0025'
base_src='H:\\FILES\\2_AUDIT DEPT\\Yr 2015\AC\\A'
base_dist='Y:\\FILES\\2_AUDIT DEPT\\Lock 2015'

print(os.pathsep)
print(os.path.join('a:', os.sep, 'c') )
print(os.path.dirname(base_src))

def replacePathSeperator(path, oldSep, newSep):
    '''correct path from '\' to '\\' on Windows
    '''
    path = path.replace(oldSep, newSep)
    return path

# print(replacePathSeperator(base_src, '/', os.sep) #os.sep is '\\' on Windows

# for folder in folders:
#     src = base_src + '\\' + folder
#     dist = base_dist + '\\' + folder
#     try:
#         shutil.copytree(src, dist)
#         #try the move()
#         shutil.move(dist, base_dist + '\\move\\')
#         print('Copy '+ folder +' is ok')

#     except (FileExistsError):
#         print('there is an error on coping ' + folder)

#     finally:
#         pass