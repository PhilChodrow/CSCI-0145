# install the pillow and numpy modules
# download middimage at
# https://raw.githubusercontent.com/PhilChodrow/CSCI-0145/main/lecture-scripts/middimage.py
# download the file at
# https://raw.githubusercontent.com/PhilChodrow/CSCI-0145/main/assets/img/jorts.jpeg
# save as jorts.jpeg

import middimage as mi

# a simple image: 2x2 pixels
pixels = [[0, 255], [255, 255]]
im = mi.MiddImage(data = pixels)
im.show()

# a simple color image: 1x2 pixels

pixels = [[[150, 20, 180], [250, 150, 150]]]
im = mi.MiddImage(data = pixels)
im.show()

# activity: modify the pixel values to be:
# your favorite color
# your partner's favorite color

# image from file: a beautiful orange boy
im = mi.open("jorts.jpeg")
im.show()

# each pixel of im contains three values (RGB)
im[100, 200]


# modifying an image: changing RGB values
for i in range(40, 70):
    for j in range(30, 80):
        im[i,j] = [40, 200, 17]

im.show()


