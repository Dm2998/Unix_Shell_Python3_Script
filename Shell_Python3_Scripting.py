# 1. In a Linux environment create a Python script with a list containing following directory names:
# o [‘testdir1’, ‘testdir2’, ‘testdir3’, ‘testdir4’, ‘testdir5’]. Note: lower case.

# 2. Using a loop; for each item in the list, use a subprocess call to create a directory with the name in
# upper-case (use the string method for case conversion)
# 3. Once the directories have been created use a subprocess calls to:
# a) Show the current disk usage in human readable format.
# b) List the directory contents to show the new directories (long format).
# c) System date and time
# d) Show the current username

#!#/usr/bin/env python3

import subprocess
import os
import datetime
directory_name = ['testdir1', 'testdir2', 'testdir3', 'testdir4', 'testdir5']


def create_directory(directory_name):
    for name in directory_name:
        subprocess.call(['mkdir', name.lower()])
        print('Directory created: ', name.lower())
    return directory_name

def show_disk_usage():          
    subprocess.call(['df', '-h'])
    
def list_directory_contents():
    subprocess.call(['ls', '-l'])
    print('Directory contents: ', directory_name)
   
     
def directory_date_time():
    subprocess.call(['ls', '-l'])
    print(datetime.datetime.now())
    
def show_current_username():
    subprocess.call(['whoami'])
    print(os.getlogin())

if __name__ == '__main__':
    directory_name = create_directory(directory_name)
    show_disk_usage()
    list_directory_contents()
    directory_date_time()
    show_current_username()
