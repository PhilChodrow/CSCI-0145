"""
--------------------------------------------
HOMEWORK 4: Working with Lists and Iteration
--------------------------------------------

In this assignment, you'll practice several simple patterns for working with
lists and for-loops. You'll also write a few list comprehensions. If you're up
for a challenge, you can write a function to estimate the number of syllables in
a word. 
"""

"""
PROBLEM 1 (40 points)
---------------------

In this problem, you'll write several functions that perform common and
important operations with lists. You should solve all of these problems with
for-loops (not list-comprehensions, which you'll learn about in another problem
on this assignment). 

HINTS: 

- You can test whether an object x is a string like this: type(x) == str
- Many of the solutions to these problems will look pretty similar to each
  other. That's intended! The idea is to give you some practice.  
"""

def contains_string(input_list):
    """
    returns True if input_list contains any strings, and False otherwise
    
    ARGUMENT input_list:, a list
    
    RETURNS: boolean, whether or not any element of input_list is a string
    """
    pass # delete and replace with your code

def all_strings(input_list):
    """
    returns: True if ALL elements of input_list are strings, and False otherwise
    
    ARGUMENT input_list:, a list
    
    RETURNS: boolean, whether or not all elements of input_list are strings
    """
    pass # delete and replace with your code

def starts_with(input_list, char):
    """
    given an input_list of strings, return only the elements of the list that
    begin with the specified character char. 
    
    ARGUMENTS: input_list, a list of strings char, a character (i.e. a string of
    length 1)
    
    RETURNS: a list containing only the elements of input_list that begin with
    char
    """
    pass # delete and replace with your code

def greet_names(name_list):
    """
    given a name_list of names, return a list of the same length containing
    messages of the form "hello [name]!" 
    
    ARGUMENTS: name_list, a list of names (strings)
    
    RETURNS: a list containing messages of the form "hello [name]!" for each
    name in name_list
    
    EXAMPLE: greet_names(["Angelique", "Nora"]) ["Hello Angelique!", "Hello
    Nora!"]
    """
    pass # delete and replace with your code

def only_positive(input_list):
    """
    given an input_list of numbers (integers or floating point numbers), return
    only the positive elements of the list
    
    ARGUMENTS: input_list, a list of numbers (integers or floats)
    
    RETURNS: a list containing only the positive elements of input_list
    
    EXAMPLE: 
    
    only_positive([-6, 4, 1, 0, 87]) [4, 1, 87]
    """
    pass # delete and replace with your code

def positive_indices(input_list):
    """
    given an input_list of numbers (integers or floating point numbers), return
    only the *indices* of the positive elements of the list
    
    ARGUMENTS: input_list, a list of numbers (integers or floats)
    
    RETURNS: a list containing the indices of the positive elements of
    input_list
    
    EXAMPLE: 
    
    positive_indices([-6, 4, 1, 0, 87]) [1, 2, 4] # indices corresponding to 4,
    1, and 87
    """
    pass # delete and replace with your code
    

def add_lists_entrywise(list_1, list_2):
    """
    add two lists of numbers (of equal lengths) together
    
    ARGUMENTS: list_1, a list of integers or floats list_2, a list of integers
    or floats. Assumed to have the same length as list_1
    
    RETURNS: a list containing the sums of the corresponding entries in list_1
    and list_2
    
    EXAMPLE: 
    
    L1 = [1,   2,    3] L2 = [2.2, 3.3., 4.4]
    
    add_lists_entrywise(L1, L2) [3.2, 5.3, 7.4]
    """
    pass # delete and replace with your code

def dot_product(list_1, list_2):
    """
    compute the dot product of two lists of numbers of equal length the dot
    product is obtained by multiplying corresponding entries and then adding up
    the results. 
    
    For example: 
    
    L1 = [1, 2, 3] L2 = [4, 5, 6]
    
    dot_product(L1, L2) = 1*4 + 2*5 + 3*6 = 32
    
    The dot product is a very important operation in math, physics, and data
    science. 
    
    ARGUMENTS list_1, a list of integers or floats list_2, a list of integers or
    floats. Assumed to have the same length as list_1
    
    RETURNS: an integer or float, the dot product of list_1 and list_2
    """
    pass # delete and replace with your code


"""
PROBLEM 2 (16 points)
---------------------

In this problem, we'll learn to use list comprehensions. A list comprehension is
a shortcut way to produce a list using a for-loop. Here's an example. Suppose
I'd like to create a list containing the even integers up to a specified value.
Here's a way that we've seen before: 

"""

def even_integers(up_to):
    even_integer_list = []
    for i in range(up_to + 1):
        even_integer_list.append(2*i)
    return even_integer_list

"""
Nothing wrong with this! But list comprehensions give us a shorter way: 
"""

def even_integers_2(up_to):
    return [2*i for i in range(up_to + 1)]

"""
Look how simple that is! List comprehensions are an example of "syntactic
sugar": a feature of Python that isn't actually needed, but makes code easier
and more fun to write. 

Please review Section 3 of our lecture notes on lists, which addresses this
topic: 

https://avaccari.gitlab.io/csci-0145/sp22/notes/lists.html

Then, please write functions that produce the required results, using list
comprehensions. You should NOT use any for-loops to solve these problems, except
for ones contained "inside" list comprehensions. 
"""

def squares(up_to):
    """
    return all the squared numbers up to and including integer up_to in a list
    
    ARGUMENT: up_to, integer, the largest number whose square to include in the
    list
    
    RETURN: a list containing the square numbers starting at 1 and up to
    up_to**2
    
    EXAMPLE: square(5) [1, 4, 9, 16, 25]
    
    HINT: range(1, up_to)
    """
    pass # delete and replace with your code

def powers_of_two(up_to):
    """
    return all the powers of two up to and including power up_to, in a list. 
    
    ARGUMENT: up_to, integer, the largest power of two to include in the list
    
    RETURN: a list containing the powers of two, starting at 2**0 and up to
    2**up_to
    
    EXAMPLE: 
    
    powers_of_two(5) [1, 2, 4, 8, 16, 32]
    """
    pass # delete and replace with your code

def greet_names_2(name_list):
    """
    exactly the same functionality as greet_names() from Problem 1, implemented
    using a list comprehension
    """
    pass # delete and replace with your code

def starts_with_2(input_list, char):
    """
    exactly the same functionality as starts_with() from Problem 1, implemented
    using a list comprehension
    """
    pass # delete and replace with your code

def add_lists_entrywise_2(list_1, list_2):
    """
    exactly the same functionality as add_lists_entrywise() from Problem 1,
    implemented using a list comprehension
    """
    pass # delete and replace with your code

def positive_indices_2(input_list):
    """
    exactly the same functionality as positive_indices() from Problem 1,
    implemented using a list comprehension.
    """
    pass # delete and replace with your code

def only_positive_2(input_list):
    """
    exactly the same functionality as only_positive() from Problem 1,
    implemented using a list comprehension. 
    """

    pass # delete and replace with your code

def dot_product_2(list_1, list_2):
    """
    exactly the same functionality as dot_product() from Problem 1, implemented
    using a list comprehension. 
    
    HINT: try sum([1, 2, 3]) and see what happens
    """
    pass # delete and replace with your code

"""
PROBLEM 3 (10 points)
---------------------

Suppose you flip a fair coin. The probability of getting heads is 50%. What if
you flip the same coin and get heads again? And again? And again? 

How many times would you have to flip the coin to get 10 heads in a row? 

This kind of question has answers that you can study in the mathematical subject
of *probability*. But if we can program, we can actually simulate this process
*without* any math. 

In this problem, we'll write a function called time_to_n_heads(). This function
should simulate flipping a coin over and over until a "streak" of n heads in a
row occurs. It should then return the total number of flips. 

Here's the algorithm you should implement: 

start a variable counting the number of heads in a row equal to 0 start a
variable counting the total number of flips equal to 0

while number of heads is less than the input n: 
    add 1 to the number of flips "flip a coin" using the choice() function (see
    hint) if the coin comes up heads: 
        add 1 to the number of heads in a row. 
    otherwise, if the coin comes up tails: 
        reset the count of number of heads in a row to 0
return the total number of flips

HINT: 

Begin your solution with the line

from random import choice

to get access to Python's random functions. Then, you can use the choice()
function to "flip the coin." Specifically, the line

flip = choice([0, 1])

will result in a variable flip that has 50% chance of having value 0 and 50%
chance of having value 1. Treat 1 as being "heads." So, you can check if flip ==
1 as a way of checking whether the "coin" came up heads.  

HINT: 

It's not a coincidence that my description of the algorithm uses the word
"while." 
"""

from random import choice
def time_to_n_heads(n):
    """
    simulate the number of flips required for a fair coin to come up heads n
    times in a row. 
    
    ARGUMENT: n, integer. The coin is flipped until a streak of n heads in a row
    occurs
    
    RETURN: integer, the total number of coin flips performed in the simulation
    """
    pass 



"""
PROBLEM 4 (5 points)
--------------------

This is a challenge problem that is worth only a small number of points. You
should only attempt this problem after you've worked on the other ones and
checked them in the autograder. 

In this problem, we'll write a function that estimates the number of syllabus in
an English word. English is a very unpredictable language with lots of
exceptions and special cases, so our function is going to be imperfect. Here's
how we'll define it: 

- A *vowel* is one of the letters "a", "e", "i", "o", "u", or "y". A *consonant*
  is any letter of the English alphabet that is not a vowel. 
- We define a *syllable* is an uninterrupted sequence of one or more vowels. 

So, your task in this problem is to write a function that can count the number
of uninterrupted sequences of vowels in an input word. 

For example, the word "bookkeeper" contains three uninterrupted sequences of
vowels: 

- "oo"
- "ee"
- "e"

So, according to our definition, this word has 3 syllables. 

**Our definition is not perfect**, and gives the wrong answers sometimes. For
example, "tone" has two sequences of vowels ("o" and "e"), but is pronounced
with only one syllable. On the other hand, "giant" has a single sequence of
vowels ("ia"), but is pronounced with two syllables. 

Write a function called estimate_syllables() that returns the number of
sequences of uninterrupted vowels in a string. 

You may assume that the argument to estimate_syllables() will always be a single
English word without spaces. 

Please make sure to include an informative docstring with your function
definition. 

HINTS: 

- This can be done using either a for-loop or with recursion. Correct solutions
  using either approach will receive full credit. Personally, I found the
  for-loop approach easier. 
- Here's how I structured my solution: 
    - I defined a variable to count the number of syllables and a variable to
      check whether the current letter was a consonant or vowel. 
    - I looped through the letters of the input string. 
        - If I saw a vowel and had previously been on a consonant, I added to my
          syllable counter variable, and swiched my consonant-or-vowel variable
          to state that I was on a vowel. 
        - If I saw a consonant, then I changed my consonant-or-vowel variable to
          state that I was on a consonant. 
    - Finally, I returned the syllable counter variable.
"""


def count_syllables(s):
    pass # delete and replace with your code