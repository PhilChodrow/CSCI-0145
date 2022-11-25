"""
-------------------------
LECTURE: Runtime Analysis
-------------------------
"""

"""
An O(n) (linear time) function to check whether an element is in a list: 
"""

def find_in_list(x, L):
    for item in L:
        if item == x:
            return True
    return False

"""
An O(log n) version using recursion: binary search
*Only works if the list L is sorted*
"""

def binary_search(x, L):
    
    # BASE CASE
    if L == []:
        return False
    if len(L) == 1:
        return L[0] == x
    
    # Recursive step
    
    midpoint = len(L)//2 # find midpoint and corresponding element
    y = L[midpoint]
    
    # if element matches, we're done
    if x == y:
        return True
    
    # recursively check list to one side of midpoint or the other
    # depending on value of comparison
    if x < y:
        return binary_search(x, L[:midpoint])
    else:
        return binary_search(x, L[(midpoint+1):])
    

"""
Experiments to compare timings
"""
import random
import time

# create a sorted list of random integers
n = 2**17 # = 131,072
L = sorted([random.randint(0, n) for i in range(n)])

# value that may or may not be in list
x = random.randint(0, 2*n)

# Time comparisons
print("\nLinear search")
print("-------------")
start = time.time()
result = find_in_list(x, L)
end = time.time()
print("Result: %r" % result)
print("Found in: %f" % (end - start))

print("\nBinary search")
print("-------------")
start = time.time()
result = binary_search(x, L)
end = time.time()
print("Result: %r" % result)
print("Found in: %f" % (end - start))