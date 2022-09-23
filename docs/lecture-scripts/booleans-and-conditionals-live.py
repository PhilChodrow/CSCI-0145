"""
------------------------------------------
Decision-Making: Booleans and Conditionals
------------------------------------------

In today's lecture, we'll introduce the key programming tools for *making
automated decisions in code.* Here's an example of a decision rule that
illustrates the components we need: 

> If I'm hungry, I'll grab a snack. 

This decision rule illustrates two items: 

- A *condition* that can be true or false. In this case, the condition is "I'm
  hungry." This is a predicate that can be either true or false (this one is
  usually true). 
- An *action* to take depending on whether the condition is true or false. 

In Python, we express conditions using *Boolean variables and expressions*. We
relate conditions to actions using `if` statements. Let's start to use these
tools. 

## Conditions: Boolean Variables and Expressions 

A `bool` (Boolean) is a Python data type that can have values `True` or `False`.
We can create `bool`s in a few ways: 

Direct assignment
"""



"""
---------------------
Functions and methods
---------------------

Many functions and methods return boolean values: 
"""


"""
--------------------
Relational operators
--------------------

Relational operators are "comparisons" between values.
Examples of English comparisons include: 

- "`x` is equal to `y`"
- "`x` is less than `y`" 
- "`x` is contained in `y`"

For example, we might express the phrase "I'm hungry" a bit more verbosely as 

> `how_Im_feeling` is equal to "hungry" 

Here are a few Python examples:
"""

# one way to test string inclusion (case-sensitive)

# tests for variables having same value 
# note: TWO equals signs!! 


# Math comparisons

## testing for odd numbers


"""
-----------------
Boolean Operators
-----------------

Booleans come equipped with some special logical operators: `not`, `and`, and
`or`. The output of a logical operator is another Boolean. 

- `not A` is `True` if `A == False`. 
- `A and B` is `True` if *both* `A == True` and `B == True`. Otherwise,
  `A and B` is `False`. 
- `A or B` is `True` if *either* `A == True` *or* `B == True`, and is `False`
   otherwise. 
"""


"""

Here's a check of whether a number is small *and* odd: 

"""

"""
-----------------------------------
Decision-Making and `if`-Statements
-----------------------------------

Now that we're able to express *conditions* (things that can be true or false),
we are ready to use them in order to choose actions to perform. Our primary
tool here is the `if` statement. 

if condition1: 
   statement1 
elif condition2: 
   statement2 
else:
   statement3 

statement4
"""


"""
A common application of if statements is to allow functions to *optionally*
print information to the user. 
"""


"""
--------------
MINI EXERCISES
--------------

if condition1: 
   statement1 
elif condition2: 
   statement2 
else:
   statement3
   
statement4

> - Which statements are executed if `condition1 is true?
> - What if `condition1` and `condition2` are both true? 
> - What if neither condition is true? 
"""


