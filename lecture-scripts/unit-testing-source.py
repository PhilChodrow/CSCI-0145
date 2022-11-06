class Vector:
    """
    A simple class representing a 2-dimensional vector
    """
    def __init__(self, x):
        """
        Initialize a Vector by specifying x and y coordinates
        """
        self.x = x
        self.y = y 
    
    def __add__(self, other):
        """
        Add two Vectors coordinate-wise, producing a new Vector. 
        """
        return (self.x + other.x, self.y + other.y) 