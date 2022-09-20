"""
------------------------------
LECTURE: Introducing Recursion
------------------------------

counting ahead of you in line...

oooooo o
|||||| |
^^^^^^ ^
012345 6       
""" 

def length(s):
    """
    compute the length of an input string
    """
    # base case: if the string is empty (contains no characters)
    #    return 0
    if s == "":
        return 0
    # recursive step: if string is not empty:
    #    return 1 + length of string AFTER 0th character
    else:
        return length(s[1:]) + 1

print("\nLength of strings")
print("-----------------")

s = "Midd"
print(length(s))
print(length(""))


"""
PART 1: String Operations
"""

def count(char, s):
    """
    compute the number of times that a character appears in a string
    """
    # if string is empty (contains no characters)
    # return 0
    if s == "":
        return 0
    # if the current (0th) character is equal to char, we found one! 
    # return the count for the *rest* of the string, plus one
    elif s[0] == char:
        return count(char, s[1:]) + 1
    # if the current (0th) character is not equal to char, then we 
    # return the count for the *rest* of the string, NOT adding one
    else:
        return count(char, s[1:])

print("\nCounting characters in strings")
print("------------------------------")

s = "to boldly go"
print(count("o", s))
print(count("z", s))

def is_palindrome(s):
    """
    return True if input string s is a palindrome
    a palindrome is a string that is the same backwards as it is forwards
    """
    if s == "":
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False
    
print("\nPalindrome detector")
print("-------------------")      
print(is_palindrome("rotator"))
print(is_palindrome("potato"))

"""
PART 2: Math
"""

def sum_up_to(n):
    """
    return the sum of all positive integers up to and including n
    """
    if n == 0:
        return 0
    else:
        return sum_up_to(n-1) + n

print("\nSum up to")
print("---------")      

print(sum_up_to(5))
print(sum_up_to(100)) # Carl Friedrich Gauss, the famous mathematician,
                      # supposedly found the formula for this when he was 6

def factorial(n):
    """
    return the *product* of all positive integers up to and including n
    by convention, factorial(n) == 1
    """
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print("\nFactorial")
print("---------")      
# factorials get very big very quickly 
print(factorial(5))
print(factorial(10))


def power(x, p):
    """
    compute x raised to the pth power, where p is a positive integer
    """
    if p == 0:
        return 1
    else:
        return x*power(x, p - 1)

print("\nPower")
print("-----")      
print(power(3, 2))
print(power(5, 3))
    
