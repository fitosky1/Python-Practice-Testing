"""
day 10
file operations
and with statements
"""
# Imports
import os

# open command simple add
file1 = open("myfile.txt", "w")
file1.write("line1\n")
file1.write("line2\n")
file1.close()
print("file1 created\n")
#
print("file1 contents\n")
os.system("cat myfile.txt")

#
file1 = open("myfile.txt", "a")
# append with for LookupError
for i in range(3, 6):
    file1.write(f"line{i}\n")
file1.close()
#
print("file1 contents after for loop\n")
os.system("cat myfile.txt")
#
# second file add reverse count from 10 to 0
# file2 = open("myfile2.txt", "w")

with open("myfile2.txt", "w") as file2:
    for i in reversed(range(11)):
        file2.write(f"{i}\n")  # not necessary to close the file!
print("file2 created")
print("file2 contents:")
os.system("cat myfile2.txt")
#
# read files
# https://www.delftstack.com/howto/python/python-readlines-without-newline/
# method1: read() as one string
with open("myfile2.txt", "r") as readfile1:
    content1 = readfile1.read()
print()
print(type(content1))
print(content1)
# print(f"{content1}")
#
# variation 1: exclude the \n
# Elegant https://newbedev.com/python-python-readlines-without-n-code-example
with open("myfile2.txt", "r") as readfile1_1:
    content1_1 = readfile1_1.read().splitlines()  # READ AS STRING
print()
print(type(content1_1))
print(content1_1)
# metehod2: readlines() as list
with open("myfile2.txt", "r") as readfile2:
    content2 = readfile2.readlines()
print()
print(type(content2))
print(content2)
# Using repr to see the canonical representation of the object
print()
print("repr content1", repr(content1))
print("repr content1_1", repr(content1_1))
print("repr content2", repr(content2))
#
# Operate with the list. In this case numbers
# to do arithmethics we need to convert the lists of strings to int
print()
print("sum with content1_1 (using for):", sum(int(i) for i in content1_1))
print("sum with content1_1 (list(map())):", sum(list(map(int, content1_1))))
#
# COPY FILES: Line by line
#
# new_file = open("new_file.txt", "w")
# with open("myfile2.txt", "r") as read_to_copy:
#     for i in read_to_copy.readlines():
#         new_file.write(i)
# new_file.close()
#
# Elegant without reading the whole file at once in memory as readlines or read methods do
# NESTED WITH
file_original = "myfile2.txt"
with open(file_original, "r") as read_to_copy:  # one line at the time
    with open("copy_" + file_original, "w") as new_file:  #
        for line in read_to_copy:
            new_file.write(line)
# print(type(new_file))
# print("new file is:", copy_myfile2.txt)
os.system("cat copy_myfile2.txt")
