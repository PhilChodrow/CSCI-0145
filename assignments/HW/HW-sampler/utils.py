import string

def load_words(path):
    with open(path, "r", encoding = "utf8") as f:
        s = " ".join(list(f.readlines()))
    for punc in string.punctuation:
        s = s.replace(punc, "")
    s = s.lower()  
    words = s.split()      
    return words

def count_syllables(s):
    num_syllables = 0
    on_consonant = True
    for letter in s: 
        if letter in "aeiouy":
            if on_consonant: 
                on_consonant = False 
                num_syllables = num_syllables + 1
        else:
            on_consonant = True
    return num_syllables
