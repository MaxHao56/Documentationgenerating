import os
import shutil

# This is for moving the files from the sphinx default and generates to sources
# It's eaiser for the commend lines to recongize the files and auto generate the rst file
files = []
length_index = 0
listdir = r'C:\Users\Max Hao\Desktop\npm_Package\Test\docs'
gotodir = r'C:\Users\Max Hao\Desktop\npm_Package\Test\docs\source'


for eachfile in files:
    old_path = listdir + eachfile[length_index][1]
    new_path = gotodir
    shutil.move(old_path,new_path)


