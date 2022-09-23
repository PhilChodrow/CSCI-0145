"""
---------------------------------------
Lecture: Recursive Graphics with Turtle
---------------------------------------

turtle is a module for creating graphics in Python. It gives us a convenient
framework for drawing pictures by moving a little "turtle" around the screen;
the picture is drawn by tracing the turtle's path. 

To use the functions in the turtle module, we need to import it. 
"""

import turtle

"""
Now we're ready! In a turtle program, we first give the turtle a sequence of
commands describing how it should move. We have commands like:

- turtle.forward(length): moves the turtle forward by the specified length
- turtle.backward(length): as above, but backwards
- turtle.left(angle): turn the turtle left by angle degrees.
- turtle.up(): "pick the turtle up" so that we can move it without tracing
- turtle.down(): "put the turtle down" so we can start tracing again. 

We then use turtle.done() to tell the
turtle that we are done drawing. Here's an example that draws a simple
horizontal line: 
"""

turtle.forward(100)
turtle.done()

"""
Here's an example that shows both turning and picking the turtle up and down. 
"""

turtle.forward(100)
turtle.up()
turtle.forward(50)
turtle.down()
turtle.left(90)
turtle.forward(100)
turtle.done()

"""
We can wrap turtle commands into functions. This lets us reuse them! 
"""

def corner(length):
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    
corner(100)
turtle.color("red")
corner(50)
turtle.done()

"""
Here's a function that draws a square:
"""

def square(length):
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)

square(100)
turtle.done()

"""
Suppose we'd like to draw some *nested squares*. Here's one way: 
"""

square(10)
turtle.up()
turtle.backward(5)
turtle.right(90)
turtle.forward(5)
turtle.left(90)
turtle.down()
turtle.color("red")
square(20)
turtle.done()

"""
It's not much fun to write this all every time. We can use recursion instead! 
"""

def nested_squares(length, level):
    if level == 0:
        turtle.done()
    else:
        square(length)
        turtle.up()
        turtle.backward(5)
        turtle.right(90)
        turtle.forward(5)
        turtle.left(90)
        turtle.down()
        nested_squares(length + 10, level-1)

nested_squares(10, 10)

"""
Here's another example: we'll use recursion to draw a fun spiral.
We're going to add some additional arguments to allow the user to control
the tightness of the spiral. 
"""

def spiral(length, angle, level):
    if level == 0:
        pass
    else:
        turtle.left(angle)
        turtle.forward(length)
        spiral(length*0.99, angle, level - 1)
        
spiral(10, 10, 1000)
turtle.done()

"""
This works, but it's often more useful to return the turtle to its
initial starting position: 
"""

def spiral(length, angle, level):
    if level == 0:
        pass
    else:
        turtle.left(angle)
        turtle.forward(length)
        spiral(length*0.99, angle, level - 1)
        turtle.backward(length)
        turtle.right(angle)

turtle.tracer(False) # cancel the animation
spiral(10, 10, 200)
turtle.color("red")
spiral(20, 15, 50)
turtle.done()