"""
------------------------------------------
LECTURE: Text Analysis With String Methods
------------------------------------------

In this lecture, we are going to work together on an example of using string
methods to achieve complicated tasks with text. The purpose of the lecture is to
(a) help you learn a few more techniques for working with strings and (b) review
some common patterns related to iteration and dictionaries. 

Our challenge today is to answer the following question: 

How many lines does each character speak in the play Hamlet, by William
Shakespeare? 

This is a long play (approximately 4,000 lines, depending on exactly how you
count), and so we definitely don't want to try to this by hand. Can a computer
program do it for us? 

Let's start by loading up the play as a string and taking a look. 
"""

def load_text(path):
    with open(path, "r", encoding = "utf8") as f:
        text = "".join(list(f.readlines()))
    return text

hamlet = load_text("hamlet.txt")

"""
We can print the string in the shell, but it might actually be easiest just to
start by looking at the original file. 

ACTIVITY: With your partner, what do you notice about the structure of this
file? 

- How do you know which lines of speech correspond to which character? 
- How do you recognize which lines of the text are character names rather than
  spoken lines?
- Which lines of text are neither character names nor spoken lines, but stage
  directions? How do you know?

Make note of the heuristics that you use to answer these questions. Can you make
them so precise that a Python program could follow them? 

We can get some insight into how we should start by splitting the text into
lines using the split() method. 
"""



"""
If this was our only data, how many characters would we say we had seen? How
many lines have been spoken by each character? 
"""

"""
-----------------------------------------
REMOVE STAGE DIRECTIONS AND SCENE HEADERS
-----------------------------------------

The stage directions are going to throw off our counts, because stage directions
are neither character names nor lines spoken by a character. We can recognize
stage directions by their first word. In this version of the play, the primary
stage directions begin with one of the following words: 
"""
sd_starts = ["Enter", "Exit", "Exeunt", "Re-enter"]

"""
Additionally, act and scene headers begin with one of the following two words: 
"""
as_starts = ["ACT", "SCENE"]

"""
Finally, some of the lines are blank: equal to ""

Let's write a function that will allow us to remove all the lines that are
either stage directions, act/scene headers, or blank. 

--------
ACTIVITY
--------

Actually, I already wrote the function you need, but...it's scrambled.
Unscramble the function! Because this one is more complex, I'm giving you the
correct indentation: you just need to figure out the order. 

        if include: 
        include = True
            if line.startswith(word):
    filtered = [] 
    return filtered 
    for line in lines: 
            filtered.append(line) 
            include = False
                include = False 
def filter_lines(lines):
        for word in sd_starts + as_starts: 
        if line == "":
"""



"""
Lovely! Now that we've done that, let's call our function to filter out unwanted
lines of text and inspect the result: 
"""



"""
Looks pretty good! 
"""

"""
-----------
COUNT LINES
-----------

Now we are finally ready to start counting the number of lines spoken by each
character in the play. For convenience, we can start with a complete cast of
characters from the play: 
"""

characters = ['BERNARDO', 'FRANCISCO', 'HORATIO', 'MARCELLUS', 'KING CLAUDIUS',
              'CORNELIUS VOLTIMAND', 'LAERTES', 'LORD POLONIUS', 'HAMLET', 
              'QUEEN GERTRUDE', 'MARCELLUS BERNARDO', 'All', 'OPHELIA', 
              'MARCELLUS HORATIO', 'HORATIO MARCELLUS', 'REYNALDO', 
              'ROSENCRANTZ', 'GUILDENSTERN', 'VOLTIMAND', 
              'ROSENCRANTZ GUILDENSTERN', 'First Player', 'Player King', 
              'Player Queen', 'LUCIANUS', 'ROSENCRANTZ: GUILDENSTERN:', 
              'PRINCE FORTINBRAS', 'First Sailor', 'Messenger', 'First Clown', 
              'Second Clown', 'First Priest', 'OSRIC', 'First Ambassador']

"""
So, now, let's get to counting lines. As a reminder, our aim is to create a
dictionary that looks like this: 

{'BERNARDO': 34, 'FRANCISCO': 10, 'HORATIO': 294, 'MARCELLUS': 60, ...}

where each key is a character and each value is the number of lines spoken by
that character. 

ACTIVITY: 

Working with the person next to you, outline an algorithmic approach to this
problem. Assume that we are going to construct a dictionary by loop through the
lines in order, so that our first line of Python code will be 

line_counts = {} for line in lines: 
    ...

Your approach should answer the following questions: 

- How will I know whether I'm on a character name or a spoken line? 
- If I am on a character name, what should I do to line_counts?
- If I am on a spoken line, what should I do to line_counts?

HINT: in your algorithm, you'll find it useful to remember the most recent
character name seen. 

Ok, now we can implement that algorithm as a function. 
"""



"""
It's nice to wrap this code up in a function, although it's unclear whether we
would reuse it very much because it takes advantage of the special structure of
this specific text file. 
"""



"""
And that's it! We have counted the number of lines per character in the play
Hamlet. Note that: 

(a) The number of lines depends on the exact formatting of the text file, so our
    results may be different from other counts. 
(b) Some "characters" are actually combinations of two characters who both speak
    the line. In a more formal analysis, we would need to account for this in
    our solution. 
"""
