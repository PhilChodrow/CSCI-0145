"""
------------------------------
LECTURE SCRIPT: More Functions
------------------------------
"""

"""
SCOPE EXAMPLE 
"""

# def increment(x):
#     """
#     an in-class demo with no docstring =(
#     """
#     x = x + 1
#     return x
# 
# x = 5
# y = 6
# z = increment(y)
# 
# print("z = " + str(z))

"""
Functions can access variables in global scope
"""
# 
def increment():
    return x + 1

x = 2
y = increment()
print(x)
print(y)


"""
However, this is not usually a great idea. It's better to pass the global
variable as an argument. 
"""

# def increment(x):
#     x = x + 1
#     return x
# 
# x = 2
# y = increment(x)
# 
# print(x)
# print(y)

"""
What do we notice about the value of x that is printed above? 
"""

"""
To change a variable defined in global scope, we need to do variable
assignment: 
"""
# x = increment(x)
# print(x)


"""
Most interesting programs use multiple functions that call each other: 
"""
# 
# def convert_temp(degrees_f):
#     """
#     convert degrees fahrenheit to degrees celsius
#     """
#     degrees_c = (degrees_f - 32) / 1.8
#     return degrees_c
# 
# def display(degrees_c):
#     """
#     print a simple string informing the user of the temperature in
#     degrees celsius. Temperature is supplied in degrees celsius. 
#     """
#     print("It is now " + str(degrees_c) + " degrees Celsius.")
#     
# def display_f(degrees_f):
#     """
#     print a simple string informing the user of the temperature in
#     degrees celsius. Temperature is supplied in degrees fahrenheit. 
#     """
#     degrees_c = convert_temp(degrees_f)
#     display(degrees_c)
    
# display_f(68)

"""
The Thonny debugger offers a nice way to visualize the flow of execution.  
"""