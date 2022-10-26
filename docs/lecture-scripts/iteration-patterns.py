"""
-------------------------------------------------
LECTURE: Common Patterns with Iteration and Lists
-------------------------------------------------

Iteration and lists are powerful tools for solving complex problems. In this
lecture, we'll work several examples of common ways to combine these tools. 

We're going to structure our discussion around the *map-filter-reduce* paradigm,
which we are currently working on in lab. 
"""

"""
--- MAP: list --> list of same length ---

A mapping operation takes a list as its primary input, and returns a new list
*of the same length* as output. It does this by applying the same operation to
every element of the input list. For example, I can divide a list of numbers.
Assume that L contains numbers (integers or floats):   
"""

def divide(L, divide_by):
    """
    return a list containing the elements of L divided by divide_by
    L is assumed to be a list of numbers
    """
    output = []                   # initialize the output list
    for num in L:                 # iterate through my input
        divided = num / divide_by # each time, compute a new value
        output.append(divided)    # add that value to an output list
    return output
    
# L = [4, 6, 7, 15]
# print(divide(L, 2))

"""
This example illustrates a very common pattern for map operations: 

1. We start by creating an empty list that will eventually hold our output. 
2. We then use a for-loop to check each item of the input, apply an operation,
   and .append() it to the output list. 
3. Finally, once the loop is complete, we return the output list, which now
   contains all the elements that we want. 
"""


"""
QUICK QUESTION: Why doesn't this function do the same thing? 
"""
def ends_with_2(L, divide_by):
    for num in L:
        return num/divide_by

"""
QUICK QUESTION: why is this function different? 
"""


"""
You can also do mapping operations with two input lists. In this case, it's
usually necessary to iterate using the range(len()) construction. 

QUICK QUESTION: Why? 
"""

def repeat(L1, L2):
    output = []
    for i in range(len(L2)):
        to_append = L1[i]*L2[i]
        output.append(to_append)
    return output

L1 = [4, 3, 2, 1]
L2 = ["Mel", "Sue", "Mary", "Paul"]
print(repeat(L1, L2))
# ["MelMelMelMel", "SueSueSue", "MaryMary", "Paul"] 



"""
------
FILTER: list --> shorter list
------

A filter operation takes a list as input and returns a list that is usually
**shorter** than the input. It does this by keeping only the elements of the
input that satisfy some criterion. 

Filter operations almost always involve an if-statement inside a for-loop. 

"""

def ends_with(L, char):
    output = []
    for word in L:
        # check if last letter is equal to char
        if word[-1] == char:
            output.append(word)
    return output

L = ["apple", "banana", "pear", "orange", "kumquat", "lychee"]
print(ends_with(L, "e"))

"""
------
REDUCE: list --> single value
------

A reduce operation takes a list as input and returns a single value, like a
number or a string. A very classical example of a reducing operation is to add
up a list of numbers, producing a single number (the total). 

For a related example, let's compute the average of a list: 
"""

def add(L):
    """
    return the sum of a list of numbers
    """
    total = 0
    for entry in L:
        total = total + entry # total += entry
    return total


L = [10, 11, 12, 13, 20]
print(add(L))

def mean(L):
    """
    return the sum of a list of numbers
    """
    total = 0
    for entry in L:
        total = total + entry # total += entry
    return total / len(L)


L = [10, 11, 12, 13, 20]
print(mean(L))





"""
ACTIVITY: 

Working with a partner, write a function to compute the *smallest* element of a
list. You can assume that the list contains numbers. 

You can use < to check whether a number is smaller than another. For example, 5
< 6 evaluates to True. 
"""

# def minimum(L):
#     smallest = L[0]
#     for entry in L:
#         if entry < smallest:
#             smallest = entry 
#     return smallest

"""
We can combine these patterns in powerful ways. For example, suppose we'd like to find the shortest string in a list that ends in "e":

1. Filter the list to contain only strings that end in "e". 
2. Find the shortest string in the filtered list. 
"""
# 
# L = ["apple", "banana", "pear", "orange", "kumquat", "lychee"]
# 
# ends_with_e = ends_with(L, "e")
# shortest    = minimum(ends_with_e)
# print(shortest)