from data import data

"""
----------
ACTIVITY 0
----------
"""




"""
----------
ACTIVITY 1
----------
"""

def well_formed(s):
    """
    a function for checking whether an input string s is a well-formed ISBN 
    according to the criteria outlined in the lab activity.
    """
    
    # check if length is 10
    digits_10 = len(s) == 10
    
    # check if all chars up to position 8 are digits
    first_9_digits = True
    for char in s[:9]:
        if char not in "0123456789":
            first_9_digits = False
            
    # check if final char is a digit or X
    last_digit_ok = True
    if s[9] not in "0123456789X":
        last_digit_ok = False
    
    # return True if all checks pass
    return digits_10 and first_9_digits and last_digit_ok

"""
----------
ACTIVITY 2
----------
"""



"""
----------
ACTIVITY 3
----------
"""

"""
----------
ACTIVITY 4
----------
"""


"""
----------
ACTIVITY 5
----------
"""

"""
----------
ACTIVITY 6
----------
"""


"""
----------
ACTIVITY 7
----------
"""






