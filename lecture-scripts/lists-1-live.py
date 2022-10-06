"""
--------------
LECTURE: Lists
--------------

So far in this class, we've focused on how to perform operations on single
pieces of data at a time. This is a good start, but the whole reason we use
computers is so that we can work on large quantities of data efficiently. 

Last time, we saw this example: 
"""

# for name in ["Xenith", "Mahmoud", "Yiran"]:
#     print("Hello " + name + "!")


"""
The object ["Xenith", "Mahmoud", "Yiran"] is a list. *Lists* are the simplest
and most flexible tool in Python for collecting large quantities of data. This
example shows us something that we'll see many more times in this course: lists
and for-loops are best friends. 

You can make lists by putting some values between square brackets, separated by
commas. 
"""

L = [1, 2, 3, 4, 5]

"""
The length of a list is just the number of items contained in it. You can get
the length using the len() function: 
"""



"""
We can treat lists a lot like strings in terms of extracting parts of them,
combining them, etc. 
"""

L1 = ["Picard", "Sisko", "Janeway", "Burnham"]
L2 = [0, 10, 20, 30, 40]

# element in position 1 of L1
# list of elements in positions 1 and 2

s = "Middlebury"
# want "id"

# want 40
L2[-1]

#
2*L2

L1 + L2

"""
--------------
Listomania
--------------

Lists also support some operations that we haven't seen before. For example, we
can modify a list by changing entries or adding new ones. 

Lists are actually the first kind of data in Python that is allowed to be
changed. Technically, lists are *mutable*: a data type that can be mutated
(changed). Integers and strings are immutable (cannot be changed). 
"""

L2[0] = 1000

L2.append("...and lots more numbers")




"""
You can even put lists in lists!
"""



"""
Lists come with many *methods*, which are functions that modify the list using
"." syntax. We'll learn lots more about methods later in the course. For now,
here's a sampling of list methods. 
"""

L = ["blue", "yellow", "red", "green"] 

print("Command                      L")
print("-------------------------------------------------------")
L.remove('yellow')                             # removes first instance of 'Kirk'
print("L.remove('yellow')          ", L)

L.pop(1)                                     # removes element in position 1 
print("L.pop(1)                    ", L)

L.insert(1,'orange')                          # adds 'Spock' in index 1
print("L.insert(1, 'orange')       ", L)
 
L.sort()                                     # sorts elements (ascending)
print("L.sort()                    ", L)

L.reverse()                                  # reverses order of elements
print("L.reverse()                 ", L)
# ---


"""
-------------------
Lists and Iteration
-------------------

Lists and iteration are **best friends**. Here's an example: 
"""

flavors = ["matcha", "chocolate", "strawberry", "oreo", "cookie dough"]

for flavor in flavors:
    print(flavor + " ice cream!")

"""
We can also use the range(len()) construction as well: 
"""

for i in range(len(flavors)):
    print("the " + str(i) + "th flavor is " + flavors[i])



"""
A common use of lists + for-loops is to create a *new* list containing
transformed data: 
"""

# challenge: double the list
L = [0, 1, 2, 3, 4, 5]



new_L = []
for entry in L:
    doubled = 2*entry
    new_L.append(doubled)
    print(new_L)





def my_function(x):
    return 2*x


my_function(4)



        
"""
This is an example of a "map" operation, and we're going to see many more
examples soon. 
"""
