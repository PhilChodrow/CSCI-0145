"""
-----------------------------
LECTURE: MORE DATA STRUCTURES
-----------------------------

In the last several lectures, we've learned about lists and worked several
examples. Lists are an extremely flexible and useful *data structure*. A data
structure is just a *structure* for holding *data*. Different data structures
have different purposes. Lists are really good for when you want to organize a
bunch of data in an *ordered relationship*: one element comes after the other.

There are LOTS of other data structures, all of which are suited for
representing different kinds of relationships between data. 

In this lecture, we'll introduce a few more data structures. We'll focus on the
most useful of these for everyday programming -- dictionaries. If you continue
in computer science, you'll take an entire class on data structures in CSCI
0201. 
"""

"""
------
TUPLES
------

A tuple is similar to a list, an ordered sequence of data. Unlike lists, tuples
are *immutable*: once created, a tuple can't be changed. For example, you can't
.append() anything to a tuple. 

A tuple is denoted by parentheses: ()
"""


"""
Tuples aren't really that useful most of the time, but there is one very
specific thing that they are extremely handy for: returning multiple values from
functions. 
"""

def quadratic_formula(a, b, c):
    """
    compute both roots of a quadratic equation a*(x**2) + b*x + c = 0
    """
    first  = (-b + (b**2 - 4*a*c)**(0.5))/2
    second = (-b - (b**2 - 4*a*c)**(0.5))/2
    return (first, second)

x_1, x_2 = quadratic_formula(4, 3, 2)    
# print(x_1, x_2)

"""
------------
DICTIONARIES
------------

Unlike tuples, dictionaries are *extremely useful* for a wide range of
programming tasks. A dictionary is a data structure that expresses a
relationship between pairs of pieces of data. For example, suppose we want to
represent the relationship between movie characters and their movies: 

Howl    --> Howl's Moving Castle 
Sophie  --> Howl's Moving Castle 
Chihiro --> Spirited Away 
Kiki    --> Kiki's Delivery Service

A dictionary is a data structure that can express this kind of relationship.
Syntactically, a dictionary is denoted by curly braces {}. It contains pairs of
data. Each pair is separated by a comma, and the two elements of the pair are
separated by a colon :. For readability, it's common to write dictionaries with
one pair on each line: 
"""

d = {"Howl"    : "Howl's Moving Castle", 
     "Sophie"  : "Howl's Moving Castle", 
     "Chihiro" : "Spirited Away", 
     "Kiki"    : "Kiki's Delivery Service"}

"""
In each pair, the first piece of data is called the *key* and the second piece
of data is called the *value*. The keys and values of a dictionary can be
extracted separately using d.keys() and d.values(): 
"""


"""
These objects aren't literally lists, but they behave in many of the same ways.
For example, you can iterate through them and convert them to lists: 
"""

"""
But of course the main thing we want to do is work with the *relationship*
between each pair. This is where dictionaries get special: you can index them
*by their keys*. 
"""


"""
This makes dictionaries very handy tools for "looking up" something in terms of
something else. For example, you could use dictionaries to keep track of due
dates of assignments for this class: 
"""

due_dates = {
    "Homework 1" : "September 17th",
    "Homework 2" : "September 24th",
    "Lab 1"      : "September 30th",
    "Lab 2"      : "October 6th"
}



"""
Unlike lists, DICTIONARIES DO NOT HAVE AN ORDER. There is no "first" element of
a dictionary. 
"""

# due_dates[0] # raises an error

"""
A very important feature of dictionaries is that they are mutable: they can be
modified, like lists. So, if you receive an extension...
"""


"""
Dictionaries have *unique keys*. If you try to add a second pair with the same
key, the pair will be overwritten. 

You can also add entirely new entries: 
"""



"""
If a dictionary doesn't have the key you're looking for, you'll get a KeyError: 
"""



"""
One thing you can do is use the dict.get() method, which allows you to specify a
value to return in case the key is not found: 
"""


 
"""
It's easy to build up dictionaries one item at a time. This makes dictionaries
especially useful for *counting things*. For example, we can write a function
that will create a dictionary counting the number of times each character occurs
in a string. We do this using a pattern that is very similar to the map and
filter operations we've seen for working with lists: we start with an empty
dictionary, and build it up one piece at a time. 
"""

    
s = "Living simply makes loving simple." # -- bell hooks



"""
Dictionaries are also very useful for *memoization*. Memoization refers to
storing prior results of computation and using them in later parts. This is a
simple idea with a big payoff for certain kinds of calculations. 

Remember the Fibonacci numbers? Our full recursive implementation looked like
this: 
"""

def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

"""
This is a totally fine definition, but as we saw in guided discovery, just
computing fib(40) or so can take a noticeably long time on your computer. The
reason is that we actually have to compute each Fibonacci number a large number
of times, leading to a total of approximately 2^n computations. But this
wouldn't be necessary if we could remember which ones we had already computed,
and just use them: 
"""

already_computed = {0 : 1, 1 : 1}

def faster_fib(n):
    
    # check: have we previously computed this Fibonacci number?
    if n in already_computed:
        return already_computed[n] # [] because this is dictionary indexing, not a funciton call
    # if not, compute it and SAVE IT for future use
    else:
        new = faster_fib(n-1) + faster_fib(n-2) # compute the new value
        already_computed[n] = new               # store it so we can use it later
        return new

# print(faster_fib(100)) # this would have taken *days* at least with the recursive definition


"""
----
SETS
----

A set is a collection of values that is *unordered*. Furthermore, all elements
of a set are unique: there can be no repetitions. 

A set is denoted by curly braces: {}
"""

s = {"Howl", "Totoro", "Chihiro", "Kiki", "Mononoke"}

"""
Like lists, sets have a len(), which is just the number of items in a set. Lists
can also be converted into sets like this: 
"""

L = ["Howl", "Howl", "Chihiro", "Kiki", "Chihiro"]
s = set(L)

"""
This gives a very handy way to count the number of *unique* elements in a list. 
"""

def num_unique(L):
    return len(set(L))

# print(num_unique(L))