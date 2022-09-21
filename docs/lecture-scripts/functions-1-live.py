"""
----------------------------------
LECTURE: Functions
----------------------------------

Let's do some examples to learn more about how write functions!

Here was our function: 

"""

def convert_temp(degrees_f):
    """
    convert degrees Fahrenheit to degrees Celsius
    
    ARGUMENT:
    degrees_f, a float or int, the temperature in degrees fahrenheit
    
    RETURN:
    float, the temperature in degrees celsius
    """
    degrees_c = (degrees_f - 32) / 1.8
    return degrees_c

"""
We can call it like this. Note that we need to print the value for it to show up
in the shell.
"""

converted = convert_temp(58)
print(converted)


converted = convert_temp(32)
print(converted)

"""
Let's learn about how the different pieces of this function work by checking on
some cases where things have gone wrong. 
"""

"""
--------------
Case 1
--------------
"""
# 
# def convert_temp(degrees_f):
# """
# convert degrees Fahrenheit to degrees Celsius
# 
# ARGUMENT:
# degrees_f, a float or int, the temperature in degrees fahrenheit
# 
# RETURN:
# float, the temperature in degrees celsius
# """
# degrees_c = (degrees_f - 32) / 1.8
# return degrees_c
# 
# new_temp = convert_temp(72)
# print(new_temp)

"""
--------------
Case 2 (look carefully at what changed)
--------------
"""
# 
# def convert_temp(degrees_f):
#     """
#     convert degrees Fahrenheit to degrees Celsius
#     
#     ARGUMENT:
#     degrees_f, a float or int, the temperature in degrees fahrenheit
#     
#     RETURN:
#     float, the temperature in degrees celsius
#     """
#     degrees_c = (degrees_f - 32) / 1.8
#     print(degrees_c)
# 
# new_temp = convert_temp(72)
# print(new_temp)
# 
# print(2*new_temp)


"""
--------------
Case 3
--------------
"""

# def convert_temp(degrees_f):
#     """
#     convert degrees Fahrenheit to degrees Celsius
#     
#     ARGUMENT:
#     degrees_f, a float or int, the temperature in degrees fahrenheit
#     
#     RETURN:
#     float, the temperature in degrees celsius
#     """
#     degrees_c = (degrees_f - 32) / 1.8
#     return degrees_c
# 
# new_temp = convert_temp(72)
# print(new_temp)

"""
---------
ACTIVITY
---------

Consider the following function: 
"""

# def test_printer():
#     """
#     a little function for an in-class question
#     """
#     print("before return")
#     return 2
#     print("after return")
#     
# x = test_printer()
# print(x)


"""
Functions can have multiple arguments! 
"""


"""
Sometimes functions will work in ways you didn't expect! This is sometimes
beneficial and sometimes a source of major headaches. 
"""

"""
ACTIVITY: write a function called says that accepts two arguments:
- name, the name of the person who will say the quote. 
- quote, a string that someone will say.

Your function should do this:

print(says("Phil", "why is this campus so big?"))
Phil says: why is this campus so big?

Make sure to incorporate all the required function components, **including a
docstring**!!
"""

