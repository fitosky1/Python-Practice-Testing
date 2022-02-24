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
    def __init__(self, arg_day, arg_month, arg_year):
        self.day = arg_day  # public and can be changed
        self.month = arg_month
        self.year = arg_year
        self._day = arg_day  # protected, changed not desired
        self.__day = arg_day  # private can't be changed or accessed
