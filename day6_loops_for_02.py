"""
Loops
For Loops 02
"""
# FOR loops
#
import random

#
rnd_list = [random.randrange(1, 50) for i in range(20)]
print("random list", rnd_list, "\n")
#
#
# Sum list
sum_list = 0
for i in rnd_list:
    sum_list += i
print("sum of list = ", sum_list)
print()
# compare within list using an input
my_number = int(input("insert a number\n"))

for i in rnd_list:
    if my_number > i:
        print("your number " + str(my_number) + " is bigger than " + str(i))
    elif my_number < i:
        print("your number " + str(my_number) + " is smaller than " + str(i))
    else:
        print("dont get it!")
