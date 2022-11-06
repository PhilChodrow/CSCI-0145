import unittest

# this special syntax means that TestVector *inherits* all the functionality
# from unittest.TestCase. So, we get to use many methods that we haven't
# explicitly wrote -- we get them for free! 
class TestVector(unittest.TestCase):
    
    # all test methods need to begin with the word "test" test methods should
    # take no additional arguments
    def test_init(self):
        """
        Check that a Vector can be initialized with user-specified x and y
        coordinates
        """
        v = Vector(2, 3)