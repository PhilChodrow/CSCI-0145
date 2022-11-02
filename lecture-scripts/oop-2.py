# -----------------------------------------
# Lecture: More Object-Oriented Programming
# -----------------------------------------

"""
In this lecture, we'll work a slightly more complicated example with object-oriented programming. We'll see an example of the OOP workflow: start with a very simple, minimal class, add a small bit of functionality, test, document, and repeat until you've obtained the desired behavior. 

We're going to implement a Point class for representing points in the 2d plane. You can find a much more complete version of this example in the official lecture notes, including docstrings: 

https://avaccari.gitlab.io/csci-0145/sp22/notes/object_oriented_programming.html

Let's start with a minimal implementation. We'll initialize a Point with two arguments: an x-coordinate and a y-coordinate. 
"""

class Point:     
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
"""
Wooo, we did it! We are already able to instantiate a Point: 
"""

p = Point(3, 4)
print(p.x)
print(p.y)

"""
This isn't very interesting though: classes that only *store data* are not very useful. Let's implement some more useful *behavior* for our class.   
"""

class Point:     
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**0.5

p = Point(3, 4)
print(p.distance_to_origin())

"""
That's more like it! 

There's still more we can do to make the Point class useful. For example, printing p or typing it in the shell doesn't lead to a very good result. When I do either, for example, I get this: 

<__main__.Point at 0x7ff5800d3550>

Not helpful! We can make something more helpful by implementing a special function called a *magic method*. A magic method is indicated by **two** underscores on either side. We've already seen an example of a magic method: __init__() is one! What makes magic methods "magic" is that they are called *implicitly*, without us explicitly calling them. In every class, instantiating it implicitly calls the __init__() method. So, when we do the line

p = Point(3, 4)

Python is *implicitly* calling Point.__init__(). There are lots of other magic methods. Let's look at another one: __repr__() controls what happens when we ask to inspect an object in the shell. 
"""

class Point:     
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**0.5
    
    def __repr__(self):
        return "A Point with x = " + str(self.x) + " and y = " + str(self.y) + "."

"""
Now when we ask to look at our point, we can see a much more useful summary. 
"""

p = Point(3, 4)
p
print(p) # also affects what happens when we print


"""
-------------------
INTERACTING OBJECTS
-------------------

A very important aspect of objects is that they can *interact with each other objects*, of the same class or different classes. 

For example, let's write a method that will allow one point to calculate its distance from another point: 
"""

class Point:     
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**0.5
    
    def distance_to_point(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5 
        
    def __repr__(self):
        return "A Point with x = " + str(self.x) + " and y = " + str(self.y) + "."

"""
QUICK ACTIVITY: Here are two points. 
"""

p1 = Point(-1, 2)
p2 = Point(11, 15)

"""
What are some quick tests you could perform to ensure that point.distance_to_point() is working correctly?
"""

first_test = p1.distance_to_point(p2) == p2.distance_to_point(p1)
second_test = p1.distance_to_point(p1) == 0

print(first_test)
print(second_test)

"""
-------
DRAWING
-------

Now let's take our Point class and give it some *visualization* capabilities. Fortunately, we know just the tools for drawing: the Turtle module! 
"""

import turtle

"""
In order to make interesting points to draw, we are going to start by giving our points additional instance variables: a size and a color. This is a great example of the interplay between attributes and behavior: in order to support the complex behavior we want, we can add new attributes. 
"""

class Point:     
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**0.5
    
    def distance_to_point(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5 
        
    def __repr__(self):
        return "A Point with x = " + str(self.x) + " and y = " + str(self.y) + "."
    
    # new methods here! 
    def coord_string(self):
        return "(" + str(round(self.x, 1)) + "," + str(round(self.y, 1)) + ")"
    
    def draw(self):
        turtle.up()
        turtle.goto(self.x, self.y)
        turtle.down()
        turtle.dot(self.size, self.color)
        turtle.write(self.coord_string())

# helper function for constructing random points
def random_point():
    colors = ["#B2AC88", "#DAA520", "pink"] # hexadecimal codes for colors
    x = random.uniform(-100, 100)
    y = random.uniform(-100, 100)
    s = random.randint(20, 70)
    color_index = random.randint(0, len(colors)-1)
    color = colors[color_index]
    return Point(x, y, s, color)


# "main loop": let's make a bunch of points and draw them! 
import random       
n_points = 10

for i in range(n_points):
    p = random_point()
    p.draw()
    
turtle.done()
