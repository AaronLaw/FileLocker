''' test shutil.copytree()
2015-08-05, by Aaron Law

cation:
As it uses Robocopy, Windows only
'''

import shutil

folder="AA0025"
base_src="H:\\FILES\\2_AUDIT DEPT\\Yr 2015\\AC\\A"
base_dist="Y:\\test"

shutil.copytree(base_src, base_dist)