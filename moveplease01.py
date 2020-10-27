#!/usr/bin/env python3

#import functions for task
import shutil
import os

#start in home dir & move file/folder
os.chdir('/home/student/mycode/')

shutil.move('raynor.obj', 'ceph_storage/')

#prompt user to give kerrigan a new name
xname = input('What is the new name for kerrigan.obj? ')

#rename kerrigan with user input
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

