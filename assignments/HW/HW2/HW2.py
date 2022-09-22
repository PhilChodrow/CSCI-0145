"""
----------
Homework 2
----------

In this assignment, you'll continue to practice writing functions. You'll also learn more about Python's error messages and solve a few simple problems using recursion. 

Like last time, your homework submission must be named "submission.py" and turned in on Gradescope. 
"""



"""
--------------------------------
Q1: Error Message Scavenger Hunt
--------------------------------
Take a moment to run the following code in Thonny: 

print(2 + " apples")

You should observe some angry-looking red text, including the phrase TypeError. 
This is an indication that we have attempted an operation on incompatible types: Python doesn't know how to add together the integer 2 and the string " apples". When an error is encountered, Python "raises" (shows) it to you, the user. 

Your aim in this question is to write functions that raise errors! Specifically, I want you to write functions that contain code that raises *specific* errors. For example: 
"""

def raises_type_error():
    """
    a function that raises a TypeError
    a TypeError is the error raised by Python when an operator or function is applied to a value of an inappropriate type
    """
    return 2 + " apples"

"""
Calling this function results in a TypeError being raised. In this problem, *that's what I want you to do!!*

Follow this same pattern to fill in the functions below. 

TESTING YOUR FUNCTIONS: 

- To test your functions, you should call them one at a time and make sure that you observe the expected errors. After you're confident in each function, you should delete or comment out the function call so that the rest of your script can run. 

"""

def raises_module_not_found_error():
    """
    a function that raises a ModuleNotFoundError
    a ModuleNotFoundError is the error raised by Python when you attempt to import a module that cannot be found
    """
    pass # replace pass with your code

def raises_index_error():
    """
    a function that raises an IndexError
    an IndexError is the error raised by Python when you attempt to access an index of a string that is out of range (e.g. too long for the string)
    """
    pass # replace pass with your code

def raises_name_error():
    """
    a function that raises a NameError
    a NameError is the error raised by Python when you attempt to refer to a variable or function that hasn't been defined yet
    """
    pass # replace pass with your code

def raises_zero_division_error():
    """
    a function that raises a ZeroDivisionError
    you can probably guess what this one means =)
    """
    pass # replace pass with your code

"""
--------------------------------
Q2: Number Flip
--------------------------------

Write a function called flip(x) that takes an integer and *reverses its digits*. 

For example: 

flip(42)  # 24
flip(378) # 873
flip(5)   # 5

Here's my suggested strategy: 

1. Use the str() function to convert the input x into a string. 
2. You can reverse a string s this way: s[::-1]. 
    - For example, "Middlebury"[::-1] is "yrubelddiM"
3. Convert the reversed string back into an integer, and return the result.

Please also add a docstring for flip(x) describing the input and output. You should also include a complete example of using the function inside the docstring. 
"""

def flip(x):
    pass # replace with your code
         # don't forget to add a docstring! 

"""
--------------------------------
Q3: Number Flip With Minus Signs
--------------------------------

Now, improve the flip(x) function so that it also accepts negative integers, preserving the sign. For example: 

flip(53)  #  35
flip(-53) # -35

Include an updated docstring. 

HINT: there are many approaches, but all the ones that I can think of use if-statements. 
"""

def improved_flip(x):
    pass # replace with your code
         # don't forget to add a docstring! 

"""
--------------------------------
Q4: Recursive Find
--------------------------------

Write a recursive function called find_char(s, char_to_find) that returns the index of character char_to_find in the input string s. For example, 

find_char("Middlebury", "l") # 4

This is because character l is in the index position 4 of the string "Middlebury". If the same character appears multiple times, return the first position. For example, 

find_char("Middlebury", "d") # 2

The character "d" also appears in index 3, but our function only finds the location of the first one (for now). 

If the character is not contained in the string, then we are going to do something new: we are going to raise an informative error message! We do this by raise-ing an IndexError. I've filled in this part of the function for you. 

The desired result is: 

find_char("Middlebury", "z")
>>> IndexError: Character not found in input string

REQUIREMENTS: 
- Your function must be recursive. Other approaches won't receive full credit. 
- You may remember the code construction "Middlebury".find("u"), which implements the same functionality. You should NOT use this construction in your solution -- I'm asking you to practice recursive problem-solving. 
- Please add a docstring describing the expected input, output, and examples. 

HINT: 
A good way to test your function is that the following code: 

s = "my string"
char_to_find = "i"

print(s[find_char(s, char_to_find)])

should always print char_to_find, provided that it's contained in s. 
"""

def find_char(s, char_to_find):
    
    # don't touch these two lines! 
    if s == "":
        raise(IndexError("Character not found in input string"))
    # fill in the rest of the recursive function below
    # there's both another part of the base case and the recursive step
    # for you to fill in. 
    
"""
--------------------------------
Q5: Improved Find
--------------------------------

Write a function called find_char_improved(s, char_to_find, mode). Here's what should happen:

- The variable mode is a string that defaults to value "first"
- If mode is "first", then the function behaves exactly like find_char from the previous part. 
- If mode is "last", then the *last* index containing char_to_find is returned, instead of the *first* index. This index is returned as a negative number. 

Examples: 

find_char("Middlebury", "d", "first") # 2, same as above

find_char("Middlebury", "d") # 2, same as above. If no user input is provided
                             # for mode, "first" is used
                             
find_char("Middlebury", "d", "last") # -7, index of *last* "d" in string, 
                                     # using negative indexing. 

Below, I've written the function declaration, including the special syntax to cause mode to have default value "first". 

REQUIREMENTS: 
- As above, your function must be recursive. In fact, a lot of the same code will work! 
- Please add a docstring describing the expected input, output, and examples. 

HINT: 
The same test from the hint for Q4 will also work well in this question. 
"""    

def find_char_improved(s, char_to_find, mode = "first"):
    pass # replace with your code! And don't forget a docstring