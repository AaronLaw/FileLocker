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


base_src1="H:\FILES\2_AUDIT DEPT\Yr 2015\AC\A".split('\\')
print(base_src1)

for element in base_src1:
    path = os.path.join(element)
print(path)


def replacePathSeperator(path, oldSep, newSep):
    '''correct path from '\' to '\\' on Windows
    '''
    path = path.replace(oldSep, newSep)
    return path

print(replacePathSeperator(base_src, '\\', '/') )
#print(replacePathSeperator(base_src, '/', os.sep) #os.sep is '\\' on Windows

def folderEncodingLookUp(folder):
    """Given a folder code, and then return a folder path

    Where the folder should be located? Its 1st char is the hints.
    For example:
    AB0079 => AC/B/AB0079
    DE0005 => DY/E/DE0005
    Ax => AC/x
    Dx => DY/x
    Fx => FC/x
    Gx => GC/x
    Yx => IY/x
    Px => PW/x
    Rx => RL/x
    Sx => SH/x
    LX => SL/x
    Tx => TO/x
    """
    # Get the 1st char of the folder
    # Lookup from the lookup table
    # Generate a path


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