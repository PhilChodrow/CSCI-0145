# -*- coding: utf-8 -*-
"""
This module provides a thin wrapper around numpy and pillow allowing us to
easily create and manipulate images.

@author: C. Andrews

2022-04-20  Modified __rep__ to fit an entire line if 8-bit mono
2022-10-20 (P. Chodrow) Modified constructor so that data will be 
automatically coerced to np.array

NOTE (P. Chodrow): If you are not able to import this module on recent 
versions of MacOS, you may need to copy/paste the code to the top of the 
file in which you are working. 
"""

import numpy as np
from PIL import Image

class MiddImage:
    
    def __init__(self, width=None, height=None, channels=3, data=None):

        if data is None:
            self.width = width
            self.height = height
            self.channels = channels
            if channels > 1:
                self._data = np.zeros((height, width, channels))
            else:
                self._data = np.zeros((height, width))
        else:
            try: 
                data = np.array(data)
            except: 
                raise(TypeError("Supplied data could not be coerced to np array"))
            
            self._data = data
            self.width = data.shape[1]
            self.height = data.shape[0]
            if len(data.shape) == 2:
                self.channels = 1
            else:
                self.channels = data.shape[2]
    
    def __getitem__(self, index):
        """
        Get the pixel at the specified 'index'.
        The 'index' should be a tuple.
        """
        return self._data[index].astype(np.uint32)
    
    
    def __setitem__(self, index, value):
        """
        Set the pixel at location 'index'.
        The 'value' should be a three channel tuple.
        """
        self._data[index] = np.uint8(value)
        
    def __repr__(self):
        """
        Show the pixels of the image.
        """
        np.set_printoptions(linewidth=(self.width + 2)*self.channels*5)
        return repr(self._data)
        
    def save(self, filename):
        """
        Save the image as 'filename' into the current working directory.
        """
        image = Image.fromarray(np.uint8(self._data))
        image.save(filename)
    
    def show(self):
        """
        Show the image.
        """
        image = Image.fromarray(np.uint8(self._data))
        image.show()
    
    def copy(self):
        """
        Returns a new MiddImage with identical contents.
        """
        new_image = MiddImage(self.width, self.height, data=self._data.copy(), channels=self.channels)
        return new_image
    
    
def new(width, height, channels=3):
    """
    Create a new image with the specified width and height.
    """
    return MiddImage(width, height, channels=channels)

def open(filename):
    """
    Open an image file located in 'filename' (which is assumed to be in the working directory
    or an absolute path.
    """
    image_data = Image.open(filename)
    raw_data = np.array(image_data)
    new_image = MiddImage(data=raw_data)
    return new_image