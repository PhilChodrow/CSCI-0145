"""
-----------------------
LECTURE: String Methods
-----------------------

In this lecture, we are going to begin a sequence of lectures and activities in
which we practice working with *strings*. We've been using strings for a long
time now, and we already know how to do things like indexing. Strings have a lot
more tricks, and today we're going to go into depth on some of them. Now that we
know object-oriented programming we're prepared to describe these tricks
accurately: *string methods*. Let's see an example: 

"""


"""
Nice and simple! s.capitalize() is a string method that returns a modified
version of the string in which the first character is capitalized. 

String methods return a modified copy of the original string. They don't modify
that string: 
"""


"""
Here are a few other string methods: 
"""



"""
There are LOTS of string methods. You can see all of them here, and you can use
help to learn what they do. 
"""



"""
---------------------
SPLITTING AND JOINING
---------------------

The str.split() method allows us to break a string apart into a list of smaller
strings, using a separator character. For example, we can make a list of
individual words by splitting on spaces (the default): 
"""




"""
The str.join() method can be used to undo str.split(). For the join method, we
need to start with the character to put BETWEEN each word, and then call .join()
with the list of words to join together. 

In the final example, the special character \n creates a new line when printed. 
"""




"""
--------
ACTIVITY
--------

Working with your partner, unscramble the code below to create a function that
returns a string containing only the words in a string less than a given length. 

return " ".join(short_words) 
short_words.append(word) 
if len(word) <= max_len:
short_words = [] 
def short_words_only(s, max_len): 
words = s.split() 
for word in words: 
"""


"""
-----------------
MULTILINE STRINGS
-----------------

In an earlier example, we saw that the special character \n creates a new line
when the string is printed. We can write strings by hand using this character,
but an easier way is to just use the ''' syntax to create a string with multiple
lines, much like we would a comment or a docstring. 
"""



"""
This is a pretty convenient way to represent text in which the line breaks
matter a lot, like poetry. Here's the poem "Joy Is Not Made To Be A Crumb" by
Mary Oliver. 
"""

poem = \
"""If you suddenly and unexpectedly feel joy, don’t hesitate.
Give in to it.
There are plenty of lives and whole towns destroyed or about to be.
We are not wise, and not very often kind.
And much can never be redeemed.
Still, life has some possibility left.
Perhaps this is its way of fighting back,
that sometimes something happens better than all the riches or power in the world.
It could be anything,
but very likely you notice it in the instant when love begins.
Anyway, that’s often the case.
Anyway, whatever it is, don’t be afraid of its plenty.
Joy is not made to be a crumb."""



"""
Let's see if we can answer some simple questions about this poem. 

1. How many lines does it have? 
2. Can we create a list containing the number of characters in each line? 
3. Can we create a list containing the number of *words* in each line? 

"""

# 1. number of lines


# 2. List of number of letters in each line


    
# 3. List of number of words in each line


"""
ACTIVITY: Working with a partner, write a quick block of code that creates a
version of the poem containing all lines containing 8 words or less. Please use
str.join()! 
"""




# alternative one-liner

    
"""
---------
F-STRINGS
---------

f-strings are a powerful tool for creating complicated, attractively-formatted
strings in Python. 

To create an f-string, just put the character f before the opening quotation
mark "
"""



"""
Why bother? f-strings can have variables directly inserted into them, without
the need for string concatenation or str() conversion. 
"""




"""
We can also use f-strings to control the *alignment* and padding of characters.
We do this by putting specifications after a colon : inside the curly braces.
There are LOTS of options for this and we're not going to go through many of
them, but our readings contain a reference. 
"""



    
"""
Here's an example of counting words in each line in our poem. 
"""

