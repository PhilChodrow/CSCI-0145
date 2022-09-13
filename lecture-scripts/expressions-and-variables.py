"""
----------------------------------
LECTURE: Expressions and Variables
----------------------------------

In this lecture, we'll: 

1. Introduce some of the most important parts of Thonny, our primary Python
   coding environment.
2. Discuss *expressions*, the simplest way to construct computational recipes.
3. Introduce *variables*, which allow us to store the results of computation for
   future use. 

# Thonny

Let's take a moment to identify and discuss the important parts of Thonny
we need to use at this stage:

- The editor window.
- The shell, which allows us to interact with the Python
  Read-Evaluate-Print-Loop (REPL).
- The play button.
- File management.

We'll get lots of practice working with each of these components very soon. 

# Expressions

An *expression* is a computational recipe. You've seen expressions in math
class. Expressions are *evaluated* to give an answer. For example, "2+2" is an
expression, and it *evaluates* to the answer 4. We can literally type this into
the Python shell and check the result.

Here's another expression:

"CSCI" + " 145"

But what about this one?

"CSCI" + 145

That's our first *error message*. The TypeError is telling us that something is
wrong with our *types*. So, what's a type? 

## Types

A *type* is a description of the kind of thing that an object is. For example,
2 and 145 are both *integers*, which is shortened to int.

QUICK ACTIVITY: Check the types of the following:

- "CSCI"
- 2.0
- True
- None

The reason we got an error earlier is that some operations only work between
variables of specific types. It can be a little surprising what operations work,
though...

3*"CS"
True - True

## Operators

We've already seen some examples of operators: symbols we can use to combine two
or more *operands* to get a result. Here are a few more: 

3*3     # multiplication
2**4    # exponentiation
4 < 5   # strict inequality
5 <= 5  # nonstrict inequality
7 // 3  # "how many times does 3 go into 7?" (integer division)
7 % 3   # "what is the remainder when 7 is divided by 3?" (modulus)
7 / 3   # "7 divided by 3, as a decimal"

These are all examples of expressions: something you evaluate to get a result.

Operators can be combined, using parentheses to group:

(2 + 3) * (4 - 2)
(-3 < 0) and (5 >= 5)
not (2022 > 2021)

The operators "and" and "not" are logical operators that take *Booleans* (things
that can be true or false) and combine them into a single true/false value.
We will play with Booleans much, much more when we get to decision-making next
week.

It's ok if you haven't digested all these operators all the way! You don't have
to memorize them yet, and you're going to get plenty of practice soon. You
should review the lecture notes for more details on each of them prior to the quiz. 

# Variables

Expressions allow us to perform computations, but:

1. They are not reusable.
2. Writing them out can get very awkward for complex calculations.

*Variables* allow us to save values for later use. 

x = 2
x

You can think of the variable x as a "box" that holds the value 2. Because x is
a box, we can take things out of it and put other things in.

x = "CS@Midd"
x

Variables allow us to organize our code, reuse computations, and make our logic
easier to understand. For example, consider the following simple program that
accepts some input about your time at Middlebury and creates a summary string. 

year_entered = 2020
print("You have been at Midd for " + str(year_entered - 2022) + " years.")


year_entered  = 2020
current_year  = 2022
years_at_midd = 2022 - 2020
print("You have been at Midd for " + str(years_at_midd) + " years.")

Notice that we gave our variables descriptive names that describe the meaning
or purpose of the values that they hold. This is good convention. We've also
allowed our variable names to contain multiple words, separated by _. This is
the approach that you are expected to use throughout CSCI 0145. 

ACTIVITY: Variable Naming

Here is a program that calculates the distance that a bicyclist travels:

x = 10
y = 2

x*y

Let's modify this program to:
- Give descriptive variable names for x and y
- save the result to a variable

It's good to have your variable names record the *units*. You can pick any units
that make sense. 

ACTIVITY: Temperature Conversion

Let's write our first Python *script*. Create a new file. Then, working with the
person next to you, write a program that converts 72 degrees degrees Fahrenheit
into degrees Celsius.

- Please include descriptive variable names.
- Once you've computed the temperature in degrees celsius, you can cause Python
to display it for you using the print command. print(x) will print the value of
x in the console. 

You can go to this url to review the formula and check your work:

https://www.metric-conversions.org/temperature/fahrenheit-to-celsius.htm


## NOTE: Assignment and Equality

Here are two expressions that look very similar: 

x = 2
x == 2

However, these two expressions do *very* different things.

x = 2 creates a variable called x that holds the value 2.
x == 2 checks whether variable x holds value equal to 2, and returns True or False. 

"""








