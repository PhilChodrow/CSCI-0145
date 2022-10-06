"""
------------------
LECTURE: Iteration
------------------

When we introduced recursion, we used it to solve problems that required us to 
perform the same kind of task over and over again. This allowed us to break 
down the solution of complicated problems into simpler problems that we could 
handle more easily. 

In this lecture, we'll introduce *iteration*. Iteration is another approach for
breaking down complex problems into simpler ones. 

We are going to consider two kinds of iteration: 

- *Definite* iteration is when we know exactly how many times we want to perform
  a task. 
- *Indefinite* iteration is when we're not sure how many times we want to
  perform a task. We're going to do it "until it's done." 
"""

"""
-----------------------------
Definite Iteration: For-Loops
-----------------------------

Let's start with an example that illustrates the main points. 

Definite iteration is performed using for-loops. A for-loop looks like this: 

for index in iterable: 
    statement_1
    statement_2
    ...
    
Our ingredients: 

- The for keyword starts the for-loop. 
- The index variable holds a value that takes on every value in iterable. The
  index is a variable, and can have any name. 
- The in keyword tells us what values the index will take in succession. 
- The *iterable* after the in keyword holds the set of values that the index
  will take.     
- The colon completes the declaration of the for-loop, similar to a function
  definition. 
- The statement_1, statement_2, etc. inside the loop will be executed once for
  each value of the index. 

Let's see a simple example: 
"""


    
"""
The stuff inside [] is a *list*, which you can think of as simply a sequence of
values. We'll learn much more about lists very soon.  

Strings can also be used as the iterable. In this case, the index will loop
through the individual characters. 
"""


"""
An especially common pattern is to loop through a *range* of numbers. The
following construction will loop through i in the values 0, 1, 2, 3, and 4 (but
NOT 5)
"""

"""
As you remember, the characters in strings can also be accessed by indexing,
like this: "CSCI 0145"[5]. This can also be a very useful way to iterate over
the letters. When we do things this way, we need to also calculate the length of
the string, which can be done using the len() function. 
"""

    
"""
For-loops can often be used to build up an *accumulation variable* that stores
some information built up across multiple loops. 
"""

# sum of the numbers 0 through 10

"""
Loops and conditionals can be a very powerful combination. 

ACTIVITY: Write a loop that prints the even numbers from 0 to 10. 

HINT: An integer i is even if i % 2 is equal to 0. 
"""



    
"""
---------------------------------
Indefinite Iteration: While-Loops
---------------------------------

Sometimes we want perform an operation over and over again, but we don't know
exactly how many times to do it. In such cases, we use a *while* loop. 

while condition:
    statement_1
    statement_2
    
The condition here is a Boolean expression that can be True or False, just like
in if statements. 

It's very important that one of the statements will eventually turn the
condition False, as otherwise the loop will execute forever! 
"""



"""
while loops can also be used to require a user to input a valid answer: 
"""

valid = False
while not valid: 
    answer = input("Please enter either a, b, c, or d.")
    valid = answer in "abcd" # Boolean statement
print("You choose option " + answer + ".")
    
"""
------------------
break and continue
------------------

Sometimes, it's handy to skip a either a single iteration of a loop, or to
simple end the entire loop. We can do this using two keywords: break and
continue. These keywords should be used with extreme caution, and should usually
be avoided. This is because they can make code very difficult to read and reason
about. 

The continue keyword will skip a single loop of an iteration: 
"""

# print a sequence of numbers, skipping multiples of 3



"""
The break keyword will completely halt an iteration, skipping any remaining
loops. 
"""



"""
Both of these examples are pretty contrived, and really should be written differently: 
"""

# first example
# for i in range(10):
#     if i % 3 != 0:
#         print(i)

# second example
# for i in range(5):
#     print(i)

"""
It can be useful to have continue and break in your toolbox, but again, they
should usually be avoided when possible. 
"""