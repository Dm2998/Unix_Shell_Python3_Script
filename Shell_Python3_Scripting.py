# 1. In a Linux environment create a Python script with a list containing following directory names:
# o [‘testdir1’, ‘testdir2’, ‘testdir3’, ‘testdir4’, ‘testdir5’]. Note: lower case.

# 2. Using a loop; for each item in the list, use a subprocess call to create a directory with the name in
# upper-case (use the string method for case conversion)
# 3. Once the directories have been created use a subprocess calls to:
# a) Show the current disk usage in human readable format.
# b) List the directory contents to show the new directories (long format).
# c) System date and time
# d) Show the current username

!#/usr/bin/env python3             # shebang line to run python3 script in linux environment.

import subprocess                    # for calling shell commands
import os                             # for getting current username
import datetime                       # for getting current date and time
directory_name = ['testdir1', 'testdir2', 'testdir3', 'testdir4', 'testdir5']


def create_directory(directory_name):           # create directories
    for name in directory_name:                 # loop through directory names
        subprocess.call(['mkdir', name.lower()])     # create directories in lower case mkdir = make directory 
        print('Directory created: ', name.lower())       # print directory name in lower case
    return directory_name

def show_disk_usage():           # show disk usage in human readable format
    subprocess.call(['df', '-h'])          # df = disk free, -h = human readable format
    
def list_directory_contents():              # list directory contents
    subprocess.call(['ls', '-l'])          # ls = list, -l = long format
    print('Directory contents: ', directory_name)
   
     
def directory_date_time():                    # show current date and time
    subprocess.call(['ls', '-l'])
    print(datetime.datetime.now())
    
def show_current_username():                   # show current username
    subprocess.call(['whoami'])                # call whoami command to show current username. linux command
    print(os.getlogin())                       # getlogin() method to show current username python method

   

if __name__ == '__main__':                   # main function to call all other functions
    directory_name = create_directory(directory_name)
    show_disk_usage()
    list_directory_contents()
    directory_date_time()
    show_current_username()
