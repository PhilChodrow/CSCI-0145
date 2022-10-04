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
    return data[:4]

def get_subject_scores(data):
    return data[4:]