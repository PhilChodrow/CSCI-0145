# --------------------------------
# GUIDED DISCOVERY 1
# STRING INDEXING AND MANIPULATION
# --------------------------------
#
# In this guided discovery exercise, you'll work with a partner to explore how 
# Python treats string variables. By the end of this assignment, you'll be able 
# to systematically extract parts of strings and create new strings using 
# simple operations.

# HOW TO SUBMIT
# To submit this assignment, upload your completed .py file  in the Guided 
# Discovery 1 activity on Gradescope.

# In our first set of exercises, we'll use the following quote by the 
# intersectional antiracist and feminist scholar bell hooks.

quote = "I will not have my life narrowed down. I will not bow down to somebody else's whim or to someone else's ignorance."

# ----------------
# PART I: INDEXING
# ----------------

# Python gives us a complex set of tools for extracting pieces of strings. 
# Let's first study *indexing*, in which we extract characters in a string by 
# specifying their position. Here's an example. Before you run this code, 
# **please take a moment to guess what character will be printed.**

print("PART I: Indexing")

print("\n(a): Single Indexing")
print("--------------------")

# Uncomment and observe the output of this line:
# print(quote[2])

# What character was printed? Was it the one you expected?

# ACTIVITY: Use this pattern to extract the following characters from the quote 
# variable:
# - "I"
# - "i"
# - " "
# - "."

# ACTIVITY: Python uses "0-based indexing." In a sentence or two, describe what
# this means based on your experiments above. Print your sentence.

# uncomment the two lines below
# response = "[REPLACE WITH YOUR SENTENCE(S)]"
# print(response)

# ACTIVITY: Uncomment and run the following code:

# print(quote[-1]) # this is called *negative indexing*

# ACTIVITY: What is your hypothesis about what happened? Test your hypothesis 
# by running a few more examples, predicting the results, and checking your 
# predictions.

# ACTIVITY: What happens when you try to extract quote[-0]?

# ACTIVITY:  Suppose you are explaining string slicing to a classmate who had 
# to miss today. In a single sentence, describe what quote[-i] means when i is 
# an integer, being careful to explain which character will be selected.

# uncomment and run
# response = "[REPLACE WITH YOUR SENTENCE(S)]"
# print(response)

print("\n(b): String Slicing")
print("-----------------")

# ACTIVITY: Uncomment and run the code below:

# print(quote[2:10]) # 2:10 is sometimes called an index range

# What happened? Which characters were printed? You might want to check quote
# [2], quote[9], and quote[10] in order to contextualize your response.

# ACTIVITY: Using this pattern, extract and print the following strings from 
# the quote variable. You might need some trial and error on this one.

# - I will not have my life narrowed down.
# - I will not bow down to somebody else's whim or to someone else's ignorance.

# ACTIVITY: This technique is called *string slicing.* Suppose you are 
# explaining string slicing to a classmate who had to miss today. In a single 
# sentence, describe what quote[i:j] means when i and j are integers, being 
# careful to explain which characters will be selected.

# uncomment and run
# response = "[REPLACE WITH YOUR SENTENCE]"
# print(response)

# ACTIVITY: Suppose that I don't know exactly how long a string is, but I want 
# to create a string that contains every character AFTER (and not including) 
# the 5th character. Using techniques from above, develop an approach and test 
# it on quote. Note that the 5th character of quote is the second "l" in "will."

print("\n\nPART II: Concatenation")
print("\n(c): Concatenation")
print("------------------")

# Uncomment and run the following code:

# string1 = "to boldly go "
# string2 = "where no one has gone before"

# print(string1 + string2)

# What do you observe? This operation is called *string concatenation.*

# ACTIVITY: Use the quote strong from before, as well as string concatenation, 
# to print the following strings.
# - There are multiple approaches. Please take a moment to think about the most 
#   efficient ones! Use negative indexing when you can.

# - I will not bow down to someone else's ignorance.
# - I will not have ignorance.
# - I will have my life.

print("\n\nPART III: If you have time")
print("\n(d): Gathering User Input")
print("---------------------------")

# The input() function allows you to interactively prompt the user to supply a 
# string. Uncomment the following three lines of code and run your script. 

# vegetable = input("If you were a vegetable, which vegetable would you be?")
# why = input("Why would you be that vegetable?")
# print("If I were a vegetable, I would be a " + vegetable + ", because " + why)

# ACTIVITY: uncomment the code below and run it. What happens?

# print(3*quote[0:11])

# ACTIVITY: Do a few more experiments if you need to. Then, write a sentence 
# describing what the output is of i*s, if i is an integer and s is a string.

# uncomment and run
# response = "[REPLACE WITH YOUR SENTENCE]"
# print(response)

# ACTIVITY: Try the following, one at a time
# 1. quote[1]*quote[0:11]
# 2. 0.99*quote[0:11]
# 3. 1.0*quote[0:11]
# 4. quote[0:11]*1.0

# Now, uncomment the below and fill in some hypothesized explanations about why 
# the Python implementers made the decisions they did with these operations.

# print("In example 1., [YOUR RESPONSE HERE]")
# print("In example 2., [YOUR RESPONSE HERE]")
# print("In example 3., [YOUR RESPONSE HERE]")
# print("In example 4., [YOUR RESPONSE HERE]")

print("\n\nPART III: If you have time")
print("\n(e): String Interpolation")
print("------------------")

# Suppose that we are creating an online ordering system in which the user can 
# ask for either hot or cold tea. We would like to print out a message for them 
# based on their selection. Suppose they choose hot tea:

temperature = "hot"

# ACTIVITY: create the string "You chose hot tea." using concatenation and the 
# temperature variable defined above. 

# String interpolation is a more convenient and flexible way to achieve a 
# similar task.
# - Note the f BEFORE the quotation mark ". 
# Try uncommenting and running the code below:

# print(f"You chose {temperature} tea.")

# ACTIVITY: in the game Mad Libs, one player is prompted to select different 
# kinds of words while the other player fills those words into some blanks 
# within some pre-existing base text. When the selected words are combined with 
# the text, a silly story emerges. For example:

# BASE TEXT
# Python is a [NOUN1] that was [VERB1] by a [ADJECTIVE1] [NOUN2] in [YEAR].

# If a user selected "sandwich," "stolen," "sentient," "raccoon," "1832", the 
# result would be "Python is a sandwich that was stolen by a sentient raccoon 
# in 1832."

# Choose a sentence, and implement a simple Mad Libs game based on your 
# sentence. You should assign variables for each of the user choices, and then 
# use string interpolation to create the final string. In the example above, 
# there should be a line of the form
# noun1 = "sandwich"
# and so on.
# Alternatively, instead of hard-coding in the strings, you could also use the 
# input() function to interactively prompt the user.

# Define some variables for nouns and verbs here

# run the below to construct your Mad Libs string.
base_string = "[YOUR STRING HERE, WITH INTERPOLATION]"
