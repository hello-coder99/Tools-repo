#!/usr/bin/env python3
from os import system,name
try:
    system('git --version')
    print("git installed in the system")
except Exception:
    print("The git is being not installed sorry")
    exit()
def linux():
    file_name=input("Enter the file name")
    f=open(file_name,'w+')
    system(f'git remote -v >> {file_name}')
    system(f'git config --list >> {file_name}')
    f.close()
    print("Thanks for using this tool")
if name!='posix':
    print("This file is not compatible in this system")
    exit()
linux()    

    

