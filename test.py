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
year = '2015'
base_path = os.path.join('H:\\', 'FILES', '2_AUDIT DEPT')

base_src='H:\\FILES\\2_AUDIT DEPT\\Yr 2015\\AC\\A'
base_dist='Y:\\FILES\\2_AUDIT DEPT\\Lock 2015'

print(os.pathsep)
print(os.path.join('a:', os.sep, 'c') )
print(os.path.dirname(base_src))


base_src1=r"H:\FILES\2_AUDIT DEPT\Yr 2015\AC\A".split('\\')
print(base_src1)

for element in base_src1:
    path = os.path.join(element)
print(path)


def replacePathSeperator(path, oldSep, newSep):
    '''correct path from '\' to '\\' on Windows
    '''
    return path.replace(oldSep, newSep)

#print(replacePathSeperator(base_src, '/', os.sep) #os.sep is '\\' on Windows

def lookupFolderEncoding(folderName):
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
    Lx => SL/x
    Tx => TO/x

    And the full path is constructed from the 2nd char too.
    For example:
    AB0079 => AC/B/AB0079
    DE0005 => DY/E/DE0005

    Algorithm:
    # Get the 1st char of the folder
    # Lookup from the lookup table
    # Generate a path
    """
    lookUpTable = { #build dict by a={}, or dict(a) to convert a sequence to a dict directly
        'A': 'AC',
        'D': 'DY',
        'F': 'FC',
        'G': 'GC',
        'L': 'SL',
        'P': 'PW',
        'R': 'RL',
        'S': 'SH',
        'T': 'TO',
        'Y': 'IY',
        }

    firstChar = folderName[0:1] # character in position 0
    secondChar = folderName[1:2] # character in position 1
    return os.path.join(lookUpTable[firstChar], secondChar)

def testlookupFolderEncoding(folderName):
    print(lookupFolderEncoding(folderName))

print('----testlookupFolderEncoding----')
testlookupFolderEncoding('AC0078')
testlookupFolderEncoding('AB0079')
testlookupFolderEncoding('DY0084')
testlookupFolderEncoding('DM0003')

def buildFolderPath(folderName):
    """Build a path base on base_path.
    Return a string represent the full path.
    """
    folderCode = lookupFolderEncoding(folderName)
    return os.path.join(base_path, 'Yr '+year, folderCode, folderName)

def testbuildFolderPath(folderName):
    print(buildFolderPath(folderName))

print('----testbuildFolderPath----')
testbuildFolderPath('AC0001')
testbuildFolderPath('AB0079')
testbuildFolderPath('DY0084')
testbuildFolderPath('DB0003')


def lookupSubfolder(path):
    """To lookup subfolders in a given path
    Given a path and return a list of subfolders
    """
    try:
        return os.listdir(path)

    except (FileNotFoundError): # path does not exist
        print ("Cannot find the given path: " + path)

def testlookupSubfolder(path):
    print(lookupSubfolder(path))

print('----testlookupSubfolder----')
# testlookupSubfolder('H:\\FILES\\2_AUDIT DEPT\\Yr 2015\\AC\\C')
testlookupSubfolder(buildFolderPath('AC0018')) # it exists
testlookupSubfolder(buildFolderPath('AC00180')) # it does not exist

def isFolderExist(path):
    """Check if folder exists
    Given a path, and return a boolean
    """
    return os.path.exists(path)

def testisFolderExist(path):
    print(isFolderExist(path))

print('----testisFolderExist----')
# testisFolderExist('H:\\FILES\\2_AUDIT DEPT\\Yr 2015\\AC\\C')
testisFolderExist(buildFolderPath('AC0018')) # it exists
testisFolderExist(buildFolderPath('AC00180')) # it does not exist


def selectSubfolder(path):
    """Interactive with user to select a given set of subfolders

    Given the path of a folder, and look into its subfolders.
    Folder only, file is not selectable!
    Return the name of selected subfolder

    Algorithm:
    Given a path
    list subfolders & subfiles of this path
    ask user to choose
    if a subfolder is chosen
        do sth...
        return the name of this subfolder
    else
        tell user only folder is selectable
        retry
    """
    lists = lookupSubfolder(path)
    i = 0
    if len(lists) != 0: # Check if the folder is empty or not
        for folder in lists:
            print(str(i) + '......' + folder)
            i = i+1
    else:
        print('Error, the folder is empty')
        raise Exception('Folder is empty')

    try:
        user_select = int(input('Which one?'))
    except ValueError as err:
        print('Value error: ' + err)
    else:
        full_path = os.path.join( path, lists[user_select]) # Create the full path of this subfolder
        if os.path.isdir(full_path):
            print('You have choose ' + lists[user_select] + '. This is:')
            print(full_path)
            return full_path

        else: # directory or nothing, that's why elif os.path.isfile() is no need
            print('Sorry, only folder is selectable')
            # retry
            lists = lookupSubfolder(path)

def testselectSubfolder(path):
    print(selectSubfolder(path))

print('----testselectSubfolder----')
testselectSubfolder(buildFolderPath('AC0018'))


def askInput(prompt, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'Y', 'yes'):
            return True
        if ok in ('n', 'N', 'no'):
            return False
        else:
            print(complaint)
            raise KeyError('uncopperative user')



def askRename(folderName, complant='Y or N, please!'):
    """Ask if user want to rename the given folder"""
    while True:
        ok = input('Do you want to rename it?')
        if ok in ('y', 'Y', 'Yes', 'yes'):
            return True
        if ok in('n', 'N', 'No', 'no'):
            return False
        else:
            print(complaint)
            raise KeyError('uncopperative user')



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