import random
from copy import copy

class CSAssignment:
    """
    docstring goes here! 
    """
    def __init__(self, due_date):
        """
        docstring goes here! 
        """
        self.done = False 
        self.score = 0
        self.due_date = due_date 
        
    def complete(self, with_collaborator = False):
        """
        docstring goes here! 
        """
        if self.done:
            print("This assignment has already been completed.")
        else:
            self.done = True 
            if not with_collaborator:
                self.score = 80 + random.randint(0, 20) 
            else:
                self.score = 90 + random.randint(0, 10)

class CSDocket:
    """
    docstring here
    """
    
    def __init__(self):
        """
        docstring here
        """
        self.assignments = []
        
    def add_assignment(self, assignment):
        """
        docstring here
        """
        self.assignments.append(copy(assignment))
        
    def complete(self, with_collaborator = False):
        """
        docstring here
        """
        not_done = [a for a in self.assignments if not a.done]
        
        if len(not_done) == 0:
            print("No incomplete assignments to complete!")
        else:
            earliest_assignment = not_done[0]
            earliest_date = earliest_assignment.due_date
            for a in not_done:
                if a.due_date < earliest_date:
                    earliest_assignment = a
                    earliest_date = earliest_assignment.due_date
            earliest_assignment.complete(with_collaborator)
            
    def average(self):
        """
        docstring here
        """
        completed_scores = [a.score for a in self.assignments if a.done]
        if len(completed_scores) == 0:
            print("No completed assignments, cannot compute an average.") 
        else:
            return sum(completed_scores) / len(completed_scores)

class CSStudent:
    """
    docstring here
    """
    def __init__(self):
        """
        docstring here
        """
        self.docket = CSDocket()
    
    def add_assignment(self, assignment):
        """
        docstring here
        """
        self.docket.add_assignment(assignment)
        
    def complete(self, collaborator = None):
        """
        docstring here
        """
        if collaborator: 
            self.docket.complete(with_collaborator = True)
            collaborator.docket.complete(with_collaborator = True)
        else:
            self.docket.complete(with_collaborator = False)
        
    def average(self):
        """
        docstring here
        """
        return self.docket.average()