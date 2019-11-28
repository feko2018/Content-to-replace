# -*- coding:utf-8 -*-

# author:feko
# time: 2019/11/28

# import package
import sys,os

# parameter declarations
arg = []
arg=sys.argv
num = 0

# parameter number judgment
if len(arg)<4:
    print("missing paramenter,exit!")
    exit()
# parameter assignment
old_str = arg[1]
new_str = arg[2]
file_name = arg[3]
old_file = file_name
new_file = file_name + '.new'

# read and create files
f = open(file=old_file,mode="r",encoding="utf-8")
f_new = open(file=new_file,mode="w",encoding="utf-8")

# Loop through the file contents by line
for line in f:
    if old_str in line:
        num = line.count(old_str) + num
        line = line.replace(old_str,new_str)
        print(num)
    f_new.write(line)
f.close()
f_new.close()

# rename for file
os.remove(old_file)
os.rename(new_file,old_file)  #open.txt.new modified into  open.txt

# print replacement times
print("replacement %s times" %(num))
