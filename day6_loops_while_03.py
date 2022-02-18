"""
Loops
WHILE Loops 02
"""
# While loops
#
import random

#
# generate random list
rnd_list = [random.randrange(1, 20) for i in range(10)]
print("random list", rnd_list)
print(len(rnd_list))
#
#
# Print elements
i = 0
while i < len(rnd_list):
    print("element", rnd_list[i])
    i += 1
# search elements
print()
i = 0
while i < len(rnd_list):
    if rnd_list[i] == 5:  # search for exact
        print("index " + str(i) + ", element " + str(rnd_list[i]))
    else:
        print("not present in index", i)
    i += 1
print()
#
# Operate with elements
i = 0
mult = 1
while i < len(rnd_list):
    mult *= rnd_list[i]
    i += 1
print("total multiplication is", mult)
print()
