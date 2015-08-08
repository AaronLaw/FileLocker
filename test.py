''' test shutil.copytree()
2015-08-05, by Aaron Law

cation:
As it uses Robocopy, Windows only
'''

import shutil

folders=['AA0008', 'AA0025']
# folder='AA0025'
base_src='H:\\FILES\\2_AUDIT DEPT\\Yr 2015\\AC\\A'
base_dist='Y:\\test'


for folder in folders:
    src = base_src + '\\' + folder
    dist = base_dist + '\\' + folder
    try:
        shutil.copytree(src, dist)
        #try the move()
        shutil.move(dist, base_dist + '\\move\\')
        print('Copy '+ folder +' is ok')

    except (FileExistsError):
        print('there is an error on coping ' + folder)

    finally:
        pass