import unittest
from source import Vector

class TestVector(unittest.TestCase):
    
    def test_init(self):
        """
        Check that a Vector can be initialized with user-specified x and y
        coordinates
        """
        v = Vector(2, 3)
        
unittest.main()