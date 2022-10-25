# install the pillow and numpy modules download middimage at
# https://raw.githubusercontent.com/PhilChodrow/CSCI-0145/main/lecture-scripts/middimage.py

import middimage as mi

# ----------------
# GREYSCALE IMAGES
# ----------------
# A simple greyscale image can be represented by a list of lists of integers
# between 0 (white) and 255 (black). 

pixels = [[0, 127, 180],     # first row of pixels
          [255, 255, 50]]   # second row of pixels

im = mi.MiddImage(data = pixels)
im.show()

# --------
# Activity
# --------
# Play tic-tac-toe with the person next to you by filling in the following
# image. The goal of tic-tac-toe is to create 3 of your color in a row (on a
# row, column, or diagonal). Partner 1 should replace the 127 with the color
# white, which is 255. Partner 2 should replace 127 with the color black, which
# is 0. 

pixels = [[127, 127, 127],
          [127, 127, 127],
          [127, 127, 127]]

im = mi.MiddImage(data = pixels)
im.show()

# ----------------
# COLOR IMAGES
# ----------------
# Color images are represented by a list of lists of lists of integers. That's a
# lot of lists! Each pixel uses three numbers to represent the RGB values. 

# # a simple color image: 2x2 pixels

pixels = [[[150, 20, 180],   # first row
           [250, 150, 150]],
          [[40, 90, 120],    # second row
           [0, 0, 100]]]

im = mi.MiddImage(data = pixels)
im.show()

# activity: modify the pixel values to be: your favorite color your partner's
# favorite color

# ------------------------------
# OBTAINING AND MODIFYING IMAGES
# ------------------------------

# download the file at
# https://raw.githubusercontent.com/PhilChodrow/CSCI-0145/main/assets/img/jorts.jpeg
# save as jorts.jpeg

# image from file: a beautiful orange boy
im = mi.open("jorts.jpeg")
im.show()

# each pixel of im contains three values (RGB)
im[100, 200]
# special syntax for working with images: im[i,j] instead of im[i][j]

# modifying an image: changing RGB values we replace the list representing the
# pixel color with a new list. 
for i in range(40, 70):
    for j in range(800, 900):
        im[i,j] = [40, 200, 17]
        # special syntax: can also do im[i,j] instead of im[i][j] 
        # ONLY works in middimage, not for general lists of lists

im.show()

# --------
# ACTIVITY
# --------

# Write a function that places a rectangle of a specified color on an image,
# using the above code as a template. Your function should take 6(!!) arguments:
# the image itself xmin and xmax, the two horizontal coordinates of the
# rectangle. ymin and ymax, the two vertical coordinates of the rectangle.
# EXAMPLE: 
# new_im = rectangle(im, 70, 90, 500, 600, [50, 10, 240]) 
# new_im.show()

def rectangle(im, xmin, xmax, ymin, ymax, color):
    # best to make a copy instead of modifying the original image
    im_copy = im.copy()
    
    # loop through the pixels remember that the FIRST index is the VERTICAL
    # coordinate. 
    for i in range(ymin, ymax):
        for j in range(xmin, xmax):
            im_copy[i,j] = color
    return im_copy

# example function call
new_im = rectangle(im, 70, 90, 500, 600, [50, 10, 240])
new_im.show()