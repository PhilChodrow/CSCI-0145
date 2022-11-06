"""
---------------------
LECTURE: Unit Testing
---------------------

In this lecture, we are going to add an important programming tool to our toolbox: unit testing. 

As you may remember, there are three major kinds of errors in programming: 

1. Syntax errors prevent our code from being executed at all. 
2. Runtime errors allow our code to be partially executed, but an error while the code is running prevents execution from being completed. 
3. Logic errors allow our code to finish executing, but an error in how we've structured the code means that the result is not what we were expecting. 

Python gives us automated tools for detecting syntax and runtime errors. What about logic errors? Especially for complex projects, how can we test whether the behaviors of our functions and classes are what we would expect? 

*Testing* refers to the practice of determining whether our code functions correctly. We've done some informal testing in this class. For example, we've run functions a few times and checked that the outputs made sense, and we've compared functions to expected outputs. *Unit testing* specifically refers to the design of small tests that check for correct behaviors of small units of code, like functions and simple classes. *Integration testing* refers to techniques for evaluating the correct behavior of large chunks of programs, and is beyond our scope for today. 

The reason we're talking about unit testing right now is that unit testing in Python is implemented with object-oriented programming. So, now that we know how to do that, we are ready to design unit tests. 

Let's get into it! Here's a simple class for representing 2d vectors. A 2d vector has an x coordinate and a y coordinate. Two vectors can also be *added* to produce a new 2d vector.  

This class is incorrect in several ways, some of which you may spot immediately. Rather than jumping right into the errors, let's spend some time going over what we would EXPECT a correct class to do. Then, we'll write code that FORMALIZES these expectations as tests. 
"""

class Vector:
    def __init__(self, x):
        self.x = x
        self.y = y 
    
    def __add__(self, other):
        return (self.x + other.x, self.y + other.y) 
    
"""
---------------------------------------------------
BRAINSTORM: how SHOULD I be able to use this class?
--------------------------------------------------- 
"""

"""
Now that we've done our brainstorming, let's start making automated unit tests that express these expectations. Here's a simple test: 
"""

import unittest

# this special syntax means that TestVector *inherits* all the functionality from unittest.TestCase. So, we get to use many methods that we haven't explicitly wrote -- we get them for free! 
class TestVector(unittest.TestCase):
    
    # all test methods need to begin with the word "test"
    # test methods should take no additional arguments
    def test_init(self):
        """
        Check that a Vector can be initialized with user-specified x and y coordinates
        """
        v = Vector(2, 3)

# this line runs all the tests  
# unittest.main()

"""
Whoops! This tells us that there's an error in our __init__() method. The reason that we know there's an __init__() issue is that __init__() is the only method of Vector called in the test_init() test, so that's the only place where something could be wrong. 

This is why we refer to *unit tests* -- they are tests of *very small* pieces of functionality. If we want to test more functionality, we don't usually add to the test method -- we write a new one. 

Note that the docstring for the test method looks a little different. The docstring is actually printed when a test is failed, so the purpose of the docstring is to describe what is being tests. 

Unit tests are almost always written in a SEPARATE Python file called tests.py or something similar. I'm keeping them in the same file this time just for the purposes of keeping these lecture notes simple. 

Before we go back and update our code, let's add more tests. An *assertion* expressed our expectation that something is true. Two of the most useful assertions are: 

- assertEqual(x, y) will cause a test to fail if x == y evaluates to False. 
- assertTrue(x) will cause a test to fail if x is a Boolean with value False. 

There are many other assertions available, but these are the most useful ones in most cases. Assertions are methods of unittest.TestCase, and are available for us to use because we designed TestVector to *inherit* all the methods of unittest.TestCase: 
"""

class TestVector(unittest.TestCase):
    def test_init(self):
        """
        Check that a Vector can be initialized with user-specified x and y coordinates
        """
        v = Vector(2, 3)
        
    def test_addition_type(self):
        """
        Check that addition produces a new Vector
        """
        v1 = Vector(2, 3)
        v2 = Vector(2, 4)
        
        v3 = v1 + v2 
        self.assertEqual(type(v3), Vector)
        
    def test_addition_arithmetic(self):
        """
        Coordinates of v1 + v2 are equal to the sum of coordinates of v1 and v2. 
        """
        v1 = Vector(2, 3)
        v2 = Vector(2, 4)
        
        v3 = v1 + v2 
        
        self.assertEqual(v3.x, v1.x + v2.x)
        self.assertEqual(v3.y, v1.y + v2.y)
        
"""
This is now a relatively comprehensive test suite. Note that the test suite is actually much longer than the code we are trying to test. This is normal! 

At this moment, we fail all three of these tests. Let's now finally fix our Vector code. 
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y) 

"""
The "OK" shown in the shell means that we didn't fail any of our tests. Lovely! 
"""

"""
-----------------------
TEST-DRIVEN DEVELOPMENT
-----------------------

It's a natural desire to see a problem and get coding immediately. However, this can make it hard to plan: we go straight from one part of the code to the next, without knowing whether changes we made in one place might break changes we made somewhere else. A more organized approach is to write unit tests BEFORE you start coding. Your aim is then to eventually write code that causes all the tests to pass. 

We are going to add some functionality to our Vector class. The *dot product* of two Vectors v1 and v2 is a single number with value v1.x*v2.x + v1.y*v2.y. The dot product is a very important operation in mathematics, physics, and data science. 

Before implementing this function, let's write some new tests FIRST. 
"""


class TestVector(unittest.TestCase):
    def test_init(self):
        """
        Check that a Vector can be initialized with user-specified x and y coordinates
        """
        v = Vector(2, 3)
        
    def test_addition_type(self):
        """
        Check that addition produces a new Vector
        """
        v1 = Vector(2, 3)
        v2 = Vector(2, 4)
        
        v3 = v1 + v2 
        self.assertEqual(type(v3), Vector)
        
    def test_addition_arithmetic(self):
        """
        Coordinates of v1 + v2 are equal to the sum of coordinates of v1 and v2. 
        """
        v1 = Vector(2, 3)
        v2 = Vector(2, 4)
        
        v3 = v1 + v2 
        
        self.assertEqual(v3.x, v1.x + v2.x)
        self.assertEqual(v3.y, v1.y + v2.y)
        
    def test_dot_product(self):
        """
        Check that the dot product of two vectors is a scalar (int or float) and has the correct value. 
        """
        v1 = Vector(2, 3)
        v2 = Vector(2, 4)
        
        d = v1.dot(v2) # this is the code we haven't written yet
        self.assertTrue(type(d) in [int, float])   # check correct type
        self.assertEqual(d, v1.x*v2.x + v1.y*v2.y) # check correct math

"""
Now that we've implemented a test, let's add the functionality to our Vector class. 
"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y) 

    def dot(self, other):
        return self.x*other.x + self.y*other.y

"""
We pass! We're now ready to move on to further development of our class. We now know that our current methods pass several simple tests of correctness. Because we formalized those tests as automated unit tests, we can check as often as we like! This is very useful during incremental development, because we know that if we make a change to some code that breaks one of our methods, for example, we'll be able to catch it quickly. 
"""

"""
And let's run our tests! 
"""
unittest.main()