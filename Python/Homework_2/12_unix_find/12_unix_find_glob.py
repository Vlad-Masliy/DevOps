import os
from fnmatch import fnmatch


def find(path, name, show_files, show_dirs):
    for dirpath, dirnames, filenames in os.walk(path):
        if show_files:
            for f in filenames:
                if fnmatch(f, name):
                    print('File', os.path.join(dirpath, f))
        if show_dirs:
            for d in dirnames:
                if fnmatch(d, name):
                    print('Directory',os.path.join(dirpath, d))


find(r'C:\Users\Vladyslav_Maslii\Desktop\Python1\Homework_2\12_unix_find', '*pyc', True, True)
