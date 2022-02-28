"""
day 11
CLASSES
"""
#
# Imports
import os

#
# one way of define a class with predefined values
# class date:
#     def __init__(self):
#         self.day = 0
#         self.month = 0
#         self.year = 0
#

# second way
class date:
    def __init__(self, arg_day, arg_month, arg_year):  # Constructor
        # self.day = arg_day  # public and can be changed
        self.month = arg_month  # Attribute
        self.year = arg_year
        # self._day = arg_day  # Protected, changed not desired (SHOULDN'T)
        self.__day = arg_day  # Private can't be changed or accessed (NOT RECOMMENDED)

    def set_day(self, new_day):  # Member method setted
        if new_day < 0:
            print("negative day")
        else:
            self.__day = int(
                new_day
            )  # With this "method" way we can change/access a private variable, within the class definition
            print("day changed")

    def get_day(self):  # Member method gettter
        return self.__day


today = date(24, 2, 2022)
print(today.month)
yesterday = date(23, 2, 2022)
print(yesterday.month)

today.set_day(-1111)
print(today)
print(today.get_day())

today.set_day(1111)
print(today)
print(today.get_day())
