# FileLocker
locking files on daily operation.

Project goals: to automate the file locking process doing everyday.
Although this program involks user interaction (the file copying is in a sequence), I should implement it in a 'leave-it-alone' style: user order the actions first, and then computer do the order with no user-interaction involked (the user can leave) and generating a report for user review it later when he come back.

## Indredient
setting as variable: base_path, curr_year, folders
shutil.treecopy(), robocopy
OO: FileLocker
** treecopy
** emailBuilder
** sendReport
optparse
json

## Reference:

Python doc:
https://docs.python.org/3/tutorial/index.html
Google: python 入門指南

To handle path sep on Windows:
Google: python path sep on windows
-> http://stackoverflow.com/questions/16010992/how-to-use-directory-separator-in-both-linux-and-windows
-> https://docs.python.org/3/library/pathlib.html#module-pathlib

I should use os.path.join() to build a path rather than I build it myself with '/' and string

How to print 'c:\some\name' on Windows? try to use a raw string:
print(r'c:\some\name')
-> http://www.pythondoc.com/pythontutorial3/introduction.html

To build a lookup table:
To analysis first, than build a data structure of key-value pairs by dict:
-> https://docs.python.org/3/tutorial/datastructures.html

To list a directory:
https://docs.python.org/3/library/os.html -> os.listdir() in https://docs.python.org/3/library/os.html#os-file-dir

Python has no switch / case:
Google: python case -> http://codingstyleguide.com/style/180/python-pythonic-way-to-implement-switchcase-statements