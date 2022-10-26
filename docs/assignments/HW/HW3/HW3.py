"""
HOMEWORK 3: Parsing Arithmetic

Take a moment and evaluate the following expression in Python: 

((((3+1)*4)*(2+1))*2)

This expression includes multiple addition and multiplication operations,
combined in somewhat complex ways. Python is able to *parse* this expression in
order to determine the correct order of operations. It then carries out these
operations in sequence to produce a result. 

A piece of code is essentially a complicated string. One of the jobs of the
Python *interpreter* (the thing that actually executes Python code) is to take
in this string and figure out what operations to perform in what sequence. 

In this homework assignment, you will write an arithmetic *parsing* function
that is able to simplify this expression, much like the interpreter would. Your 
parser will accept a string with a specific structure as input, and output a
string representing its value. Here's an example: 

expression = "((((3+1)*4)*(2+1))*2)" 
result = simplify(expression) 
print(result)

will print 96, the numerical value of the supplied expression. 

ASSUMPTIONS: 

- We are only dealing with addition and multiplication.
- Integers only, no floating point numbers (decimals) 
- EVERY addition or multiplication operation is surrounded by parentheses. That
  means that (2+2) is allowed, but 2+2 isn't. Similarly, (3*(2+2)) is ok because
  both arithmetic operations are surrounded by parentheses. 3*(2+2) is not
  allowed, because the multiplication operation is not surrounded by
  parentheses. 

The reason for these assumptions is to make your life easier!! Please try to
solve the homework with these assumptions first. You can try to handle more
general cases later if you want to. 

STRATEGY: 

Our strategy is to look for the innermost expressions surrounded by parentheses,
evaluate them, and replace them. For example, in (3*(2+2)), our first step is to
replace (2+2) with 4. This gives us (3*4), which we'll evaluate to get the final
answer of 12. If we use recursion, then we will be able to simplify even very
complicated expressions! 

This is a complex task, and so we are going to break it up into stages. 

NOTE: 
At the bottom of this file, there is a series of tests you can do for each
problem. These tests are very similar to what the autograder will do! I suggest
that you uncomment these tests as you complete each problem in order to check
your progress. 
"""

"""
PROBLEM 1: 

In several later parts of this assignment, we are going to need to determine
whether a string contains a character, and if so in what index. Implement the
find() function that I've documented for you below. 

HINT: 
You actually implemented a version of this function in HW2. This time,
I'm asking you to do it slightly differently: 

1. You should use a for-loop rather than recursion. 
2. If the searched character is not in the string, you should return None rather
   than raise an error. 

NOTE: 
You may be familiar with the string method string.find(). You should not
use this method in your solution, and should instead follow the approach written
in pseudocode in the comments. 

TARGET LENGTH: 
You can implement this function in under 10 lines of code. 
"""

def find(char, s, which = "first"):
    """
    Find the location of a character char within a string s if s contains char
    and which == "first", then the index of the first instance of char is
    returned. if s contains char and which == "last", then the index of the
    final instance of char is returned. if s does not contain char, then None is
    returned. 
    
    ARGUMENTS: char, a single character to be searched within s s,    the string
    in which char is searched which, whether the "first" or "last" instance of s
    should be returned. 
    
    EXAMPLES: 
    find("d", "Middlebury", which = "first") # 2 
    find("d", "Middlebury", which = "last")  # 3 
    find("z", "Middlebury)                   # None
    """
    pass
    
    # Approach
    # set current_index equal to None
    # loop through the characters of s
    #     if character i of s is equal to char, set current_index to i
    #     if which is set to "first", return the current_index immediately
    # if which is set to "last", return the current_index after the loop    

"""
PROBLEM 2

Let's say that a string is *compound* if it contains either "*" or "+". Complete
the function is_compound() below. 

HINT: 
USE find() FROM PROBLEM 1!!!

TARGET LENGTH: 
You can implement this function in under 5 lines of code. 
"""

def is_compound(s):
    """
    tests whether string s contains either "*" or "+"
    
    ARGUMENT: s, the string to be determined as compound or not. 
    
    EXAMPLES: 
    is_compound("(1+1)") # returns True 
    is_compound("11")    # returns False
    """    
    pass

"""
PROBLEM 3

Write a function called find_inner(s), which finds the first expression in s
that is contained within parentheses, but has no parentheses inside it. For
example, if 

s = "((1+1)+((5+3)*2))"

then find_inner(s) should return the starting and ending indices for the string
"(1+1)" contained in s. 

The result should be returned as a pair of indices corresponding to the opening
and closing parentheses. In this case: 

ix1, ix2 = find_inner(s)

results in ix1 having value 1 and ix2 having value 5. We could therefore get the
inner expression, including parentheses, like this: 

s[ix1:ix2+1] # "(1+1)"

NOTE: You don't need is_compound() in this problem but you do need find() from
Problem 1. 

HINT: 
To write a function with multiple return values, just separate what you
want to return with commas. For example: 

def multiple_return_values():
    first_value = 2
    second_value = 3
    return first_value, second_value
    
v1, v2 = multiple_return_values()
# v1 has value 2, v2 has value 3

HINT: 
I've given you pseudocode again. 

TARGET LENGTH: 
You can implement this function in under 5 lines of code. 
"""

def find_inner(s):
    """
    finds the first expression contained in parentheses that does not itself
    contain any parentheses, returning the result as the indices of the
    enclosing parentheses. 
    
    ARGUMENT: s, the string in which to seek the inner expression 
    
    EXAMPLES: 
    s = "((1+1)+((5+3)*2))" 
    ix1, ix2 = find_inner(s) # ix1 is 1, ix2 is 5
    
    s = "(((3+13)*2)+5) 
    ix1, ix2 = find_inner(s) # ix1 is 2, ix2 is 6
    """
    
    # let ix2 be the location of the first ")" you can find() 
    # if ix2 is not None: 
    #     let ix1 be the location of the last "(" in s[:ix2] 
    #     return ix1, ix2
    
    pass
    
    
    
"""
PROBLEM 4

Now we know how to pick out an expression like "(5*3)", let's write a function
called simplify_inner() to evaluate that expression. It should work like this: 

simplify_inner("(5*3)") # returns "15", as a string

NOTE: the result should be returned as a string, not an integer

ASSUMPTIONS: 

- The expression is always surrounded by parentheses: the first character is "("
  and the last character is ")"
- There is exactly one "*" or "+" in the expression, inside the parentheses. 

Your function should work for multidigit numbers: 

simplify_inner("(20*3)") # "60"

I've implemented the separate() function to help you get started. You can call
it like this: 

arg1, symbol, arg2 = separate("(20*3)")
# what are the values of arg1, symbol, and arg2 now? 

You should: 

- Test what separate() does, and check that you understand why, using the above
  example as a starting point. 
- WRITE A DOCSTRING FOR separate(). 
- Use separate() as suggested below to complete simplify_inner(). 

HINTS: 
- Your first line of the definition of simplify_inner() should probably resemble
the example using separate() from above. 
- Use int("9") to convert the strig "9" to the integer 9. Use str(9) to convert
  the integer 9 back to the string "9". 

TARGET LENGTH: 
You can implement simplify_inner() in under 10 lines of code. 
"""

def separate(expr):
    """
    WRITE A DOCSTRING HERE PLEASE!
    """
    for char in ["+", "*"]:
        loc = find(char, expr, which = "first")
        if loc: 
            return expr[1:loc], expr[loc], expr[(loc+1):-1]
    return expr

def simplify_inner(expr):
    """
    evaluate a compound expression contained in parentheses, returning the
    result as a string. 
    
    ARGUMENT: expr, the expression to be evaluated. 
    
    EXAMPLES: 
    
    simplify_inner("(20*3)") # returns "60" 
    simplify_inner("(2+7)")  # returns "9"
    """
    pass
    
"""
PROBLEM 5

Write a function called simplify_once() which takes in a string and performs a
single simplification. For example: 

s = "((2+2)*(3+2))" 
simplified = simplify_once(s) # returns "(4*(3+2))"

I've given you a pseudocode outline in the comments 
"""

def simplify_once(s):
    """
    simplify the first compound expression possible in a complicated expression s. 
    You can assume that there is at least one compound expression s. 
    
    ARGUMENT: s, the expression to be simplified
    
    EXAMPLE: s = "((2+2)*(3+2))" 
    simplified = simplify_once(s) # simplified is a string with value
    "(4*(3+2))"
    """
    # use find_inner() to locate the indices of the first expression that can be
    # simplified. 
    # use simplify_inner() to determine the simplified value of this expression 
    # create a new string in which the expression in parentheses is replaced by
    # the simplified value
    # return the simplified expression
    pass
    
"""
PROBLEM 6

Now that we know how to simplify_once(), let's simplify recursively! 

Fill in the simplify() function below, INCLUDING A DOCSTRING. Do your best to
write a docstring that makes clear the roles of the inputs and outputs, and
includes an example. You can infer this from the pseudocode. 

TARGET LENGTH: 
You can implement simplify() in under 10 lines of code. 
"""

def simplify(s, verbose = True):
    """
    PLEASE WRITE A DOCSTRING FOR SIMPLIFY HERE!
    """
    # if verbose is True, 
    #   print s (this is just for fun) 
    # BASE CASE 
    # if s is not compound (use Problem 2) 
    #   return s 
    # else (if s is compound)
    #   use simplify_once() to simplify s once 
    #   call simplify() on the result
    
    pass
        

"""
PROBLEM 7: 

Just kidding, there is no Problem 7! Great job on this assignment! Please
submit on Gradescope, check your autograder feedback, and use it to improve your
submission as needed. 
"""

"""
the code below is for testing your solutions
You can comment and uncomment the code, but modifying it is not recommended. 
"""

if __name__ == "__main__":
    # PROBLEM 1 TESTS you can uncomment these when you're ready to test your
    # problem 1 solution
    
    print("\nPROBLEM 1 TESTS")
    print("---------------")
    print(find("d", "Middlebury", which = "last")) # 3
    print(find("(", "(1+1)"))                      # 0
    print(find(")", "6"))                          # None
    
    # PROBLEM 2 TESTS
    # print("\nPROBLEM 2 TESTS")
    # print("---------------")
    # print(is_compound("(1+1)")) # True 
    # print(is_compound("11"))    # False

    # PROBLEM 3 TESTS
    # print("\nPROBLEM 3 TESTS")
    # print("---------------")
    # s = "((1+1)+((5+3)*2))"
    # ix1, ix2 = find_inner(s) 
    # print(ix1, ix2)          # (1,5)

    # s = "(((3+13)*2)+5)"
    # ix1, ix2 = find_inner(s) 
    # print(ix1, ix2)          # (2,7)
    # print(s[ix1:ix2+1])      # "(3+13)"
    
    # PROBLEM 4 TESTS
    # print("\nPROBLEM 4 TESTS")
    # print("---------------")
    
    # print(simplify_inner("(20*3)")) # "60"
    # print(simplify_inner("(2+7)"))  # "9"
    
    # PROBLEM 5 TESTS
    # print("\nPROBLEM 5 TESTS")
    # print("---------------")
    
    # s = "((2+2)*(3+2))"
    # simplified = simplify_once(s) # "(4*(3+2))"
    # print(simplified)
    
    # PROBLEM 6 TESTS
    # print("\nPROBLEM 6 TESTS")
    # print("---------------")
    
    
    # s = "((2+2)*(3+2))"
    # simplify(s, verbose = True) # prints the steps, finishing at 20. 
    """
    DESIRED PRINTED OUTPUT: 
    ((2+2)*(3+2))
    (4*(3+2))
    (4*5)
    20
    """

    # print("\n")
    
    # s = "((((3+4)*(3+1))+67)*(5+6))"
    # simplify(s, verbose = True) # prints the steps, finishing at 1045 
    """
    DESIRED PRINTED OUTPUT: 
    ((((3+4)*(3+1))+67)*(5+6))
    (((7*(3+1))+67)*(5+6))
    (((7*4)+67)*(5+6))
    ((28+67)*(5+6))
    (95*(5+6))
    (95*11)
    1045
    """