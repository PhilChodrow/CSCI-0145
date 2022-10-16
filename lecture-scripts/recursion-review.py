"""
-----------------
REVIEW: Recursion
-----------------

In this lecture session, we'll work several review examples on the topic of recursion. 
"""

"""
WARMUP: Write a recursive function absolute value function. 

This function should, given a list L of integers, return a version of that list
in which all negative numbers are replaced by their positive versions. 

For example: 

L = [-5, 4, 3, -2, 8] abs(L) >>> [5, 4, 3, 2, 8] 
"""

def abs(L):
    if L == []:
        return L
    else:
        if L[0] < 0:
            return [-L[0]] + abs(L[1:])
        else:
            return [L[0]] + abs(L[1:])

L = [-5, 4, 3, -2, 8]
print(abs(L))

"""
Let's write a recursive implementation of the modulus operator %. Our function will be called mod(), and mod(x,y) will have the same value as x % y. For example, 

mod(8, 3) 
>>> 2
"""

def mod(x, y):
    if x < y:
        return x
    else:
        return mod(x-y, y) 

"""
Many functions that we perform using for-loops can be instead performed recursively (note: this is not ALWAYS better, just different). Consider the function from a recent lecture on dictionaries. This function computes the count or frequency of each item in a string. 
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
We could instead write this function recursively! This requires passing two arguments to the function: both the string and a dictionary containing the counts. The dictionary starts off empty.  
"""

def recursive_count(s, counts = {}):

    if len(s) == 0:
        return counts 
    else:
        c = s[0]
        if c not in counts.keys():
            counts[c] = 1
        else:
            counts[c] = counts[c] + 1
        return recursive_count(s[1:], counts)

counts_2 = recursive_count(s)
print(counts == counts_2)

"""
This implementation is neither simpler nor faster, but it is recursive! 
"""
