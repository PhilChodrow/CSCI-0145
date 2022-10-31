# ---------------------------------------
# Introducing Object-Oriented Programming
# ---------------------------------------

# A good way to write classes is to start very small!!
# note the use of self to describe data and methods that "belong to" the object
class Bird:
    
    def __init__(self, genus, species):
        self.genus = genus
        self.species = species
        
    def binomial_nomenclature(self):
        return self.genus + " " + self.species
        
genus    = "Melopsittacus"
species  = "undulatus"
parakeet = Bird(genus, species)

# when calling a method, we use the syntax object.method()
bn = parakeet.binomial_nomenclature()
print(bn)

# a slightly more complex Bird class
class Bird:
    
    def __init__(self, genus, species, color, can_fly = True):
        self.genus = genus
        self.species = species
        self.color = color
        self.can_fly = can_fly
        self.num_eggs = 0
    
    def binomial_nomenclature(self):
        return self.genus + " " + self.species
    
    def describe_fly(self):
        if self.can_fly:
            is_able = ""
        else:
            is_able = "not"
        return "This bird is " + is_able + " able to fly."
    
    def describe_eggs(self):
        s = "So far, this bird has laid " + str(self.num_eggs) + "eggs. "
    
    def describe(self):
        s = "This bird is "
        s += self.binomial_nomenclature() + ". "
        s += "Currently, this bird is " + self.color + ". "
        s += self.describe_eggs()
        s += self.describe_fly()
        return s

    def lay_egg(self):
        self.num_eggs +=1
        
    def molt(self):
        self.color = "brown"
        
