# --------------------------------------------
# HOMEWORK 6: Geometric Graphics
# --------------------------------------------

# In this homework assignment, you'll use what we've learned about image
# representation and iteration to create simple geometric graphics. You'll also
# get a bit of practice with object-oriented programming. 

# SUBMITTING THIS HOMEWORK: In this homework, you will need to submit BOTH your
# code AND the images that you create. Please make sure to save them an upload
# them to Gradescope along with your code. 

# Unlike most homework assignments, this one is NOT autograded. We'll be looking
# at your code and the images you submit. 

# needed for the first few problems make sure you have middimage.py in the same
# directory as your submission.py file. 
import middimage as mi

# ---------------------
# PROBLEM 1 (15 points)
# ---------------------

# In this problem, you'll unscramble a function that takes an image as input and
# returns a copy of that image containing a square. At the URL below, you can
# see an example of the result of calling this function. 

# https://raw.githubusercontent.com/PhilChodrow/CSCI-0145/main/assignments/HW/HW6/img/square.png

# I produced this image by using the following three lines of code: 
# blank = mi.new(500, 500) 
# with_square = square(blank, 250, 250, 100, [180, 20, 180])
# with_square.show()

# Here's the scrambled function

# for col in range(im.width): 
# return im2
# for i in range(3): 
# for row in range(im.height): 
# if abs(row - y) <= side_length//2 and abs(col - x) <= side_length//2: 
# im2 = im.copy() 
# im2[row, col, i] = color[i] 
# def square(im, x, y, side_length, color):

# WHAT YOU SHOULD DO
# 1. Write an unscrambled version of the function below. You need to figure out
#    the order of the lines and the indentation, but you should NOT modify any
#    of the code beyond that. 
# 2. Write a docstring for the function that includes: 
#    - A description of *all 5* of its arguments. Your description should allow
#      a user to call your function without reading the code. 
#    - A description of the return value of the function

# For your convenience, the tests at the bottom of the assignment will save your
# images in the supplied img folder. They'll call your functions and save the
# result in the folder. You can check that folder to see if your images look
# correct. 

# [YOUR FUNCTION HERE]

blank = mi.new(500, 500) 
with_square = square(blank, 250, 250, 100, [180, 20, 180])
with_square.show()

# ---------------------
# PROBLEM 2 (15 points)
# ---------------------

# Now, write a function called square_sequence(). Your function should return an
# image containing a sequence of nested squares with alternating colors, like
# this one: 

# https://raw.githubusercontent.com/PhilChodrow/CSCI-0145/main/assignments/HW/HW6/img/squares.png

# Your function should take *seven* arguments. 
# 1. im, the image to modify. 
# 2. x, int, the horizontal coordinate (column) of the center of the squares. 
# 3. y, int, the vertical coordinate (row) of the center of the squares. 
# 4. bandwidth, int, the thickness of each square. 
# 5. max_length, int, the size of the largest square. 
# 6. color1, list, the first color to alternate.
# 7. color2, list, the second color to alternate.

# For example, I produced the image linked above using the following code: 
# blank = mi.new(500, 500) 
# x = 250 
# y = 250 bandwidth = 20 
# max_length = 400 
# purple = [180, 20, 180] 
# white = [255, 255, 255] 
# with_seq = square_sequence(blank, 250, 250, bandwidth, max_length, purple, white) 
# with_seq.show()

# STRATEGY: 

# 1. Create a copy of the image. 
# 2. Set current_length equal to max_length, and set i = 0
# 3. As long as current_length > 0
#    - if i is even, set color = color1
#    - if i is odd, set color = color2
#    - Add a square to the image using your function from the previous problem,
#      using current_length as the side length and the current color. The square
#      should be centered at the pixel (x, y). 
#    - Reduce the current length by the bandwidth
#    - Increase i by 1
# 4. Return the modified image

# YOU ARE NOT REQUIRED TO WRITE A DOCSTRING FOR THIS PROBLEM

# [YOUR FUNCTION HERE]

# ---------------------
# PROBLEM 3 (10 points)
# ---------------------

# Write a function called disc() that draws a colored, circular disc in a
# supplied image. Here's an example of an image constructed using this function: 

# https://raw.githubusercontent.com/PhilChodrow/CSCI-0145/main/assignments/HW/HW6/img/disc.png

# This function should take five arguments: 
# 1. im, the image to modify. 
# 2. x, int, the horizontal coordinate (column) of the center of the disc. 
# 3. y, int, the vertical coordinate (row) of the center of the disc. 
# 4. radius, int, the radius of the disc. 
# 5. color, list, the color of the disc. 

# I made the example above using the following code: 
# purple = [180, 20, 180]
# blank = mi.new(500, 500) 
# with_disc = disc(blank, 250, 250, 150, purple)
# with_disc.show()

# HINT: The body of your function should have ONLY 1 LINE that is different from
# the square() problem in Problem 1. 
 
# HINT: You may find it useful to recall the inequality that defines a disc in
# the plane: https://en.wikipedia.org/wiki/Disk_(mathematics)#Formulas You can
# use the "closed disc" formula for this problem. 

# [YOUR FUNCTION HERE]

# ---------------------
# PROBLEM 4 (10 points)
# ---------------------

# Write a function called bullseye() that creates colorful bullseye patterns
# composed of layered discs, like this one: 

# https://raw.githubusercontent.com/PhilChodrow/CSCI-0145/main/assignments/HW/HW6/img/bullseye.png

# Your function should accept 7 arguments: 
# 1. im, the image to modify. 
# 2. x, int, the horizontal coordinate (column) of the center of the bullseye. 
# 3. y, int, the vertical coordinate (row) of the center of the bullseye. 
# 4. bandwidth, int, the thickness of each layer of the bullseye. 
# 5. max_radius, int, the radius of the outermost circle of the bullseye. 
# 6. color1, list, the first color to alternate.
# 7. color2, list, the second color to alternate.

# I made the example above using the following code: 
# bandwidth = 20 
# max_radius = 200
# purple = [180, 20, 180]
# white = [255, 255, 255]
# with_bullseye = bullseye(blank, 250, 250, bandwidth, max_radius, purple,
# white) 
# with_bullseye.show()

# HINT: Use your disc() function from the previous problem. HINT: This function
# should look almost exactly like square_sequence(). 

# [YOUR FUNCTION HERE]

# ----------------------------
# TESTS (for your convenience)
# ----------------------------

if __name__ == "__main__":
    
    purple = [180, 20, 180]
    white = [255, 255, 255]
    bandwidth = 20
    x = 250
    y = 250
    
    # PROBLEM 1
    blank = mi.new(500, 500)
    side_length = 200
    try: 
        with_square = square(blank, x, y, side_length, purple)
        with_square.save("img/with_square.png")
    except NameError:
        print("NameError raised: possibly you haven't completed Problem 1 yet?")
    
    # PROBLEM 2    
    blank = mi.new(500, 500)
    max_length = 400
    
    try: 
        with_seq = square_sequence(blank, 250, 250, bandwidth, max_length, purple, white)
        with_seq.save("img/squares.png")
    except NameError:
        print("NameError raised: possibly you haven't completed Problem 2 yet?")

    # PROBLEM 3
    blank = mi.new(500, 500)
    try: 
        with_disc = disc(blank, 250, 250, 150, purple)
        with_disc.save("img/disc.png")
    except NameError: 
        print("NameError raised: possibly you haven't completed Problem 3 yet?")

    # PROBLEM 4
    blank = mi.new(500, 500)
    max_radius = 200    
    try: 
        with_bullseye = bullseye(blank, 250, 250, bandwidth, max_radius, purple, white)
        with_bullseye.save("img/bullseye.png")
    except NameError: 
        print("NameError raised: possibly you haven't completed Problem 4 yet?")
    
    