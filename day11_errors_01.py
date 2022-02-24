"""
day 11
exceptions
raise errors
BE CAREFUL!!
"""
# Imports
import os, random

#
nr_to_guess = random.randint(1, 10)

## Not breakable !!!!
# loop = 0
# i = 0
# while i < 5:
#     try:
#         in_user = int(input("guess a number from 1 to 3\n"))
#         if in_user not in [1, 2, 3]:
#             raise RuntimeError("wrong range")
#             print("you guessed the number!")
#     except RuntimeError:
#         print("Sorry, no numbers except 1,2,3")
#     except ValueError:
#         print("Wrong input")
#     else:
#         if nr_to_guess == in_user:
#             # print("try again")
#             i += 1
#     finally:
#         loop += 1
#         print(f"{loop} iterations happened")
