"""
-----------------
REVIEW: Recursion
-----------------

In this lecture session, we'll work several review examples on the topic of
recursion. 
"""

"""
WARMUP: Write a recursive function absolute value function. 

This function should, given a list L of integers, return a version of that list
in which all negative numbers are replaced by their positive versions. 

For example: 

L = [-5, 4, 3, -2, 8] abs(L) >>> [5, 4, 3, 2, 8] 
"""

def abs(L):
    pass 
    # base case: L is the empty list
    
    
    # recursive step: return a list where: 
    # 1. the 0th element has its sign adjusted if necessary
    # 2. the abs() function is called on all of L *except* the first element. 
    

# test: uncomment when you're ready L = [-5, 4, 3, -2, 8] print(abs(L))

"""
It can be useful to write recursive functions with multiple arguments. Let's
write a recursive implementation of the modulus operator %. Our function will be
called mod(), and mod(x,y) will have the same value as x % y. For example, 

mod(8, 3) >>> 2
"""

def mod(x, y):
    pass
    # base case: what should the result be if x < y? 
    
    
    # recursive step: use the mathematical relationship mod(x, y) = mod(x-y, y)
    

"""
Many functions that we perform using for-loops can be instead performed
recursively (note: this is not ALWAYS better, just different). Consider the
function from a recent lecture on dictionaries. This function computes the count
or frequency of each item in a string. 
"""

def character_counts(s):
    d = {}
    for char in s: 
        if char not in d.keys():
            d[char] = 1
        else: 
            d[char] = d[char] + 1  
    return d
    
s = "Living simply makes loving simple." # -- bell hooks
counts = character_counts(s)
print(counts)

"""
We could instead write this function recursively! This requires passing two
arguments to the function: both the string and a dictionary containing the
counts. The dictionary starts off empty.  
"""

def recursive_count(s, counts = {}):
    pass
    # base case: if s is empty, return the counts

    
    # recursive step: process a single character of s and add it to counts call
    #     the function recursively on the REST of s, with the updated counts

# counts_2 = recursive_count(s) print(counts == counts_2)

"""
This implementation is neither simpler nor faster, but it is recursive! 
"""
