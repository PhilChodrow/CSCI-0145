import random

FIRST_YEAR      = 0 
SECOND_YEAR     = 1
THIRD_YEAR      = 2
FOURTH_YEAR     = 3
LITERATURE      = 4
SCIENCE         = 5
MATH            = 6
SOCIAL_STUDIES  = 7
ELECTIVES       = 8

EXAMPLE = [3.4, 3.3, 2.7, 3.6, 4.1, 3.5, 2.8, 3.2, 3.0]

def get_year_scores(data):
    """
    given a list containing applicant scores, return a list containing only the average GPAs for their first, second, third, and fourth years of secondary school. 
    
    ARGUMENT: 
        data, a list containing numbers 
    
    RETURN: 
        a list containing only the first four elements of data
        
    ASSUMPTIONS: 
        the first four elements of data contain the scores for the applicants first, second, third, and fourth years
        
    EXAMPLE: 
    
    EXAMPLE = [3.4, 3.3, 2.7, 3.6, 4.1, 3.5, 2.8, 3.2, 3.0]
    get_year_scores(EXAMPLE)
    """
    return data[:4]

def get_subject_scores(data):
    """
    given a list containing applicant scores, return a list containing only the average GPAs for their subject areas (literature, science, math, social studies, and electives) in their third and fourth years. 
    
    ARGUMENT: 
        data, a list containing numbers 
    
    RETURN: 
        a list containing only the last five elements of data
        
    ASSUMPTIONS: 
        the last five elements of data contain the scores for the applicants five subject areas
        
    EXAMPLE: 
    
    EXAMPLE = [3.4, 3.3, 2.7, 3.6, 4.1, 3.5, 2.8, 3.2, 3.0]
    get_subject_scores(EXAMPLE)
    """
    return data[4:]

def create_app():
    """
    return a random example application using a random number generator. 
    """
    return [2 + 2*random.random() for i in range(9)]

def create_apps(num_apps):
    """
    return many random example applications
    the return value is a list of length num_apps, each entry of which is an example application. 
    """
    return [create_app() for i in range(num_apps)]

def print_apps(apps, first_n):
    """
    print a desired number of applications from a list in a slightly more readable format. 
    """
    for app in apps[:first_n]:
        print([round(x, 1) for x in app])