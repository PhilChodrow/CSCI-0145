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

x = True 
y = False 

"""
---------------------
Functions and methods
---------------------

Many functions and methods return boolean values: 
"""

m = "Middlebury"
m.startswith("M")

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
"Midd" in m
"midd" in m

# tests for variables having same value 
# note: TWO equals signs!! 

m == "Middlebury" 
m == "Midd"
m[:4] == "Midd"

m != "Midd"

# Math comparisons
len(m) == 10
0 < 1
1 == 1.0
7 < 8 < 9

## testing for odd numbers

9 % 2 == 1
10 % 2 == 1

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

not True
not False

True and False
True or False
"""

Here's a check of whether a number is small *and* odd: 

"""
def small_odd(n):
    return (n < 10) and ((n % 2) == 1)

small_odd(9)
small_odd(11)
small_odd(4)

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

def sign_of(n):
    if n > 0:
        print("n is positive")
    elif n < 0:
        print("n is negative")
    else:
        print("n is 0")

"""
A common application of if statements is to allow functions to *optionally*
print information to the user. 
"""

def double(x, message = True): # default value: message is True if no value supplied
    if message:
        print("Doubling your input, which was " + str(x))
    return 2*x

print(double(2, True))
print(double(6, False))
print(double(10))

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


