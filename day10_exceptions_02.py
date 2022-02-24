"""
day 10
exceptions
BE CAREFUL!!
"""
# Imports
import random

#
i = 0
Base = random.randint(1, 10)
while i < 5:
    try:
        Number = int(input("Type a number "))
        Divi = Base / Number
    except ZeroDivisionError:
        print("Division by Zero")
    except ValueError:
        print("Value type error")
    else:
        print("Division is", Divi)
    finally:
        print(f"End of iteration {i}")
    # print(Divi)
    i += 1
