from os import path, mkdir, move
import sys
import subprocess
import pkg_resources

required = {'PIL', 'shutil'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

#make directorys for startprocess.py to search through
mkdir('./icons')
mkdir('./images')

print('Installation Complete')
