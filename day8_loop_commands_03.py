"""
Python commands within Loops
"break", "continue" and "pass"
"""
#
import random

#

list1 = list(random.sample(range(1, 100), 15))
print(list1)
#
sum = 0
for i in list1:
    print(i)
    sum += i
    if sum < 0:
        pass
    elif sum > 600:
        print("we reach 600")
        break
    elif sum > 200 and sum < 300:
        print("within 200 and 300")
        continue
    else:
        print(sum)
