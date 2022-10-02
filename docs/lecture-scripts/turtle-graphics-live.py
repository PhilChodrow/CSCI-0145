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

# turtle.forward(100)
# turtle.done()


"""
Here's an example that shows both turning and picking the turtle up and down. 
"""

# turtle.forward(100)
# turtle.up()
# turtle.forward(50)
# turtle.down()
# turtle.left(90)
# turtle.forward(100)
# turtle.done()


"""
We can wrap turtle commands into functions. This lets us reuse them! 
"""

def corner(length):
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    
# corner(100)
# turtle.color("red")
# corner(50)
# turtle.done()



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

# square(100)
# turtle.done()


"""
Suppose we'd like to draw some *nested squares*. Here's one way: 
"""

# square(50)
# turtle.up()
# turtle.backward(5)
# turtle.right(90)
# turtle.forward(5)
# turtle.left(90)
# turtle.down()
# turtle.color("red")
# square(60)
# turtle.done()

"""
It's not much fun to write this all every time. We can use recursion instead! 
"""

def nested_squares(length, level):
    """
    Draw a sequence of nested squares
    
    ARGUMENTS:
    length, integer, the length of the innermost
            square
    level, integer, the number of squares to draw
    
    EXAMPLE:
    nested_squares(10, 10)
    """
    
    # base case
    if level == 0:
        turtle.done()
        
    # recursive step
    else:
        # draw the square
        square(length)
        
        # pick the turtle up and move it
        turtle.up()
        turtle.backward(5)
        turtle.right(90)
        turtle.forward(5)
        turtle.left(90)
        turtle.down()
        
        nested_squares(length + 10, level - 1)
        
# nested_squares(10, 10)




"""
Here's another example: we'll use recursion to draw a fun spiral.
We're going to add some additional arguments to allow the user to control
the tightness of the spiral. 
"""

def spiral(length, angle, level):
    
    # base case
    if level == 0:
        pass
    
    # recursive step
    else:
        turtle.forward(length)
        turtle.left(angle)
        spiral(length*0.99, angle, level - 1)
        turtle.right(angle)
        turtle.backward(length)

# spiral(20, 10, 100)
# turtle.done()

turtle.tracer(False)
spiral(10, 10, 200)
turtle.color("red")
spiral(20, 15, 50)
turtle.color("blue")
spiral(15, 12, 100)
turtle.done()





