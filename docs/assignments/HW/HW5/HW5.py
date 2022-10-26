"""
--------------------------------------------
HOMEWORK 5: Dictionaries, Data Representations
--------------------------------------------

In this assignment, you'll use dictionaries and iteration to solve several
problems involving text analysis: the use of computational tools to learn more
about bodies of text. You'll also further explore binary representations of
data. 
"""

"""
---------------------
PROBLEM 1 (30 points)
---------------------

In class, we practiced converting integer *from* binary into decimal
representations. In this problem, you'll write a function called to_binary()
that converts a decimal integer to a binary representation. This function should
accept an integer argument and return a string of 0s and 1s. For example: 

to_binary(16) >>> "10000"

to_binary(123456) >>> "11000000111001"

Here's my suggestion: 

- Call the argument to convert n. 
- Initialize an empty string to hold the final answer. 
- Determine the largest power p of 2 that is not larger than the input. 
- In a loop: 
    - If 2**p is less than n, add "1" to the string and remove 2**p from n. 
    - Otherwise, add "0" to the string. 
    - Reduce p by 1. 

HINT: This is a good application for a while-loop. 

Please include a docstring! Your docstring should describe the overall purpose
of the function, the argument (including its data type) and the return value
(including its data type). 

NOTE: It is possible to do this problem using recursion instead of a loop. Extra
credit if you do!! 
"""

        
"""
---------------------
PROBLEM 2 (10 points)
---------------------

# INTRODUCTION

To start this problem, please start by finding a large file of plain text that
you would like to study. One easy way to find such a file is to visit Project
Gutenberg's list of popular books: 

https://www.gutenberg.org/ebooks/search/?sort_order=downloads

Click a title you'd like to use, and find the Plain Text UTF-8 version. See an
example of what it should look like here: 

https://www.gutenberg.org/files/11/11-0.txt

Choose File --> Save As, and save the file with the filename story.txt. You
should save it in the same directory as your homework file.  You can open this
file in a text editor. You might wish to do so and delete the language at the
beginning and end of the file about Project Gutenberg, so that you can focus on
the text. 

We are going to study *word frequencies* in this text. By the end of this
sequence of problems, you'll be able to print a list describing the most common
words in the text. 

The following code loads your file and divides it into a list of lowercase
words. For example, if your file was very small and contained only the words
"The cat sat on the mat", we would have: 

words = load_words("text.txt") words >>> ["the", "cat", "sat", "on", "the",
"mat"]
"""

import string

def load_words(path):
    with open(path, "r") as f:
        s = " ".join(list(f.readlines()))
    for punc in string.punctuation:
        s = s.replace(punc, "")
    s = s.lower()  
    words = s.split()      
    return words

"""
WHAT YOU SHOULD DO

Now, write a function called count_words() whose argument is a list of words and
whose return value is a dictionary where each key is a word and each key's value
is the number of times that word appears in the list. This is sometimes called a
*concordance*. For example, using the words variable from above:

count_words(words) >>> {"the" : 2, "cat" : 1, "sat" : 1, "on" : 1, "mat" : 1}

PLEASE INCLUDE A DOCSTRING. Your docstring should contain a sentence that simply
describes the purpose of the function; a description of the argument (including
its data type); and a description of the return value (including its data type). 

HINT: This problem is closely related to Example 3 from our lecture notes on
dictionaries: 

https://avaccari.gitlab.io/csci-0145/sp22/notes/data_structures_and_references.html

You will likely find this example to be helpful in the next several problems. 

HINT: This is a problem that could be addressed using recursion, but Python
places a limit on how many times a function can be called recursively. Because
of this, I recommend that you use a loop instead. 
"""





"""
---------------------
PROBLEM 3 (10 points)
---------------------

A *stopword* is a word that that is considered to be uninteresting for text
analysis. Examples of English stopwords include "the," "but," "and," "her," and
so on. You can find a list of common stopwords at the bottom of this file. 

Write a function called remove_stopwords(). This function should take two
arguments: 

- A dictionary of counts, such as would be returned by count_words()
- A list of stopwords. 

Your function should return a dictionary of counts, NOT INCLUDING stopwords.
With the example before: 

stopwords = ["the", "on", "and"] d = count_words(words) d = remove_stopwords(d,
stopwords) d >>> {"cat" : 1, "sat" : 1, "mat" : 1}

The counts for "the" and "on" have been removed because they are stopwords. 

PLEASE INCLUDE A DOCSTRING. Your docstring should contain a sentence that simply
describes the purpose of the function; a description of the argument (including
its data type); and a description of the return value (including its data type). 
"""




"""
---------------------
PROBLEM 4 (20 points)
---------------------

Write a function called print_top_words(). This function will print (NOT return)
the words with the highest counts in the data set. This function should accept
two arguments: 

- d, a dictionary of counts such as would be returned by count_words() or
  remove_stopwords()
- num_words, the number of words to print

The function should print the top num_words words in the data set, in descending
order, along with their counts. For example, I obtained these counts on the text
of Grimm's Fairy Tales: 

print_top_words(d, 10)

little               388 
away                 278 
king                 264 
man                  214 
old                  201 
time                 184 
day                  181
come                 170 
home                 170 
shall                168

For full credit, PLEASE USE RECURSION. It's also possible to do this problem
using a loop; loop-based solutions will received most but not all of the credit. 

To do this recursively: 

- if the input dictionary is not empty and num_words is positive:
    - Find the word with the highest count in the dictionary, and print it. 
    - Remove that word from the dictionary. 
    - Reduce num_words by 1. 
    - Call print_top_words() with the modified dictionary and reduced num_words

HINTS: 

print(f"{word:20} {count}") will print your word and count in a pretty way, like
shown above. 

It's ok if your function prints MORE than the specified number of words, in case
some words are tied for 10th. 

The largest value in the dictionary d can be found using max(d.values()). 

d.pop() can be used to remove key-value pairs from dictionaries. 
"""




"""
--------------------
PROBLEM 5 (10 points)
--------------------

Copy and paste the printed output of print_top_words(d, 10) below, in order to
show the 10 most common words in your text.  
DO NOT CHANGE THE NAME OF THE VARIABLE s
"""

s = """
[YOUR TOP WORDS HERE]
"""


"""
--------------------
EXAMPLE TESTS
--------------------

The code below this line is for your benefit as you write and test your
functions. It is not recommended that you modify this code in any way. The
autograder tests are similar to the tests shown here. 
"""


if __name__ == "__main__":
      
    print("\n---------------")
    print("Problem 1 Tests")
    print("---------------\n")
    
    try:
        d = {123 : "1111011", 
             16 : "10000", 
             12345 : "11000000111001"}
        
        for n in d: 
            answer = to_binary(n)
            print(f"Expected : to_binary({n}) = {d[n]}")
            print(f"Found    : to_binary({n}) = {answer}\n")
            
            
    except NameError: 
        print("to_binary() not yet implemented.")
        
    print("\n---------------")
    print("Problem 2 Tests")
    print("---------------\n")
    try: 
        path = "story.txt"
        words = load_words(path)
        
    except:
        print("issue opening file: make sure it's called story.txt and saved in the same directory as your Python file")
    
    try: 
        print("Showing counts of a few selected words")
        print("--------------------------------------")
        d = count_words(words)
        samples = list(d.keys())[:5]
        for sample in samples: 
            print(f"{sample:25}{d[sample]}")
    except NameError:
        print("count_words() not yet implemented")
    
    stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "said", "came", "went", "one", "‘i", "would", "could", "go", "took", "upon", "saw"]
    
    print("")
    print("---------------")
    print("Problem 3 Tests")
    print("---------------")
    try: 
        d = remove_stopwords(d, stopwords)
        
        found = False
        for word in stopwords: 
            if word in d:
                found = True
        if not found: 
            print("No stopwords detected in dictionary!")
        
    except NameError:
        print("remove_stopwords() not yet implemented")
    
    print("")
    print("---------------")
    print("Problem 4 Tests")
    print("---------------")   
    try: 
        print("")
        print("Top 10 Words In Text")
        print("--------------------")
        print_top_words(d, 10)
    except NameError:
        print("print_top_words() not yet implemented")
        
    print("---------------")
    print("Problem 5 Tests")
    print("---------------")   
    if len(s.split("\n")) < 10:
        print("It looks like you have fewer than 10 top words!")
    else:
        print("Thanks for showing your 10 top words!")