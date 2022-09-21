"""
In this assignment, you'll hone skills like writing functions, manipulating strings, and performing conditional execution. You'll also practice using the Thonny debugger and reflecting on your experience with automated decision systems. 
"""

"""
Q1: Expressions
In this question, you'll do a series of short exercises to practice evaluating Python expressions. 
"""

"""
First, please describe both the *value* and *type* of the output for each of the expressions below. For example, the expression 5*1 has value 5 and a type of int.  

1. 12 / 3
Returned value and type:

2. 12 / 5
Returned value and type:

3. 12 // 5
Returned value and type:

4. 12 / 3.0
Returned value and type:

5. 4 + 6 * 2 / 2 ** 3
Returned value and type:

6. 5 - 2 <= 4
Returned value and type:

7. not 5 < 6 and 23 >= 19
Returned value and type:
"""

"""
Next, what is the value stored in each of the variables x and y once the lines of code have been evaluated? Beside each line, write a comment describing the value of both x and y. You will learn the most if you try to do this *without* evaluating the code in Thonny. You can use Thonny to check once you're done. 
"""

x = 3
y = 9
x = 3 * x - y/2
y = y - 5


"""
Q2: Unit Displays

In this problem, you will write a function called convert_height that displays a height supplied in inches into a pleasantly readable string. Here's an example of what we're going for: 

convert_height(73) # someone is 73 inches tall
> "6 feet and 1 inch"

In case you're not familiar with feet-inch measurement, an inch is equal to 2.54cm. A foot is equal to 12 inches. 

SPECIFICATIONS: 

Your function should display the largest number of feet that total less than the current height. For example, this would be wrong: 

convert_height(50)
> "3 feet and 14 inches"

The correct result would be "4 feet and 2 inches". 

Your result should never include "0 feet" or "0 inches." Instead, these units should not be printed at all, like this: 

convert_height(60)
> "5 feet"

convert_height(5)
> "5 inches"

Please include correct English pluralization of feet and inches. In particular:
1 foot, not 1 feet. 
1 inch, not 1 inches. 
2 feet, not 2 foot. 
2 inches, not 2 inch. 


CODE REQUIREMENTS: 

Your function should include a simple docstring describing its inputs, outputs, and assumptions. 

Your solution should demonstrate: 

- At least one use of if-else. 
- At least one use of a boolean operation: and, or, or not. 

DOCUMENTATION REQUIREMENTS: 

Please include a helpful docstring that describes the overall purpose, input, output, and assumptions of the function. 

Please include a few comments that help make clear the purpose of each block of code. You should have a comment roughly every 3-5 lines of code. 

ASSUMPTIONS: 

You may assume that the user will always input an integer (whole number) that is not negative. 

HINT: 
Consult the Python documentation on numbers (https://docs.python.org/3/tutorial/introduction.html#numbers) for the // and % operators. Can you use them to design your solution? 

HINT: 
You will find it useful to write some lines of code in which you *call* your function in order to check for expected behavior. 

"""


def convert_height(height_in_inches):
    """
    [REPLACE WITH YOUR DOCSTRING]
    """
    pass # replace with your solution
    
    

"""
Q3: Debugging Practice

Your friend has written a function to compute the distance between two two-dimensional points. Each point is specified by an x-coordinate and a y-coordinate. 

In case you need to remember this formula, you might want to check here: 

https://www.calculatorsoup.com/calculators/geometry-plane/distance-two-points.php

Your friend's function displays many good ideas, but unfortunately it's not completely correct! You should do the following: 

- Fix the function so that it correctly outputs the distance between points (x1, y1) and (x2, y2)
- Include short comments describing each change you made. You should include **at least four** such comments. 
- Improve the docstring so that it describes: 
    - In simple language, what the function does. 
    - What data types must be supplied, and any assumptions that are made. 
    - The data type and meaning of the returned value. 
    
NOTE: it is strongly suggested that you use the Thonny debugger for this activity. 
"""

def distance(x1, y1, x2, y2):
    """
    calculate the distance
    """
    
    deltaX = x2 - X1
    deltaY = y2 - x1
    distance_squared = deltaX^2 + deltaY^2
    distance = distance_squared**(0.5)
    print(dist)

"""
Q4: Automated Decision Systems

We are surrounded by automated decision systems. Just at Midd, your housing, your eligibility for financial aid, and even your ability to enroll in this course were partially controlled by algorithms. 

- Think of a time when an automated decision system made a decision that you felt was *fair*. It should be a decision that relates to you or someone you know. It can also be one you read about, although not in this article. What are your reasons for thinking this decision was fair? Write at least *three* complete sentences answering these questions and save them in the string variable FAIR below. 
- Now, try to think of a time when an automated decision system made a decision that you felt was *unfair*. Repeat the above prompt, saving your response in the string variable UNFAIR below. 
"""

FAIR = ""
UNFAIR = "" 