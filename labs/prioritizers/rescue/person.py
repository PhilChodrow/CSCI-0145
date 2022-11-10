import random

""" Packages all the info needed for a character.

Every scenario is composed of characters - many of which are people. Each
of those people can contain a variety of characteristics. The Person class
is used to represent the many pieces of information for people. 

Attributes:
	charType (string): 'human', 'you', 'cat', 'dog'
	age (string): humans can be a 'baby', 'child', or 'adult'
	profession (string): adults are assigned a profession: 'doctor', 'CEO',
		'criminal', 'homeless', 'unemployed', 'unknown'
	gender (string): 'male', 'female', or 'nonbinary' 
"""

class Person:
	def __init__(self, charType=None, age=None, profession=None,
		gender=None):
		''' Create a character by randomly selecting their attributes

		All of the parameters in this method are OPTIONAL. This means that by
		default, a random character is made if no information is given. For
		example:
			character = Person()

		However, you can also create a custom character by filling in any
		number of those parameters. For example, the following code would
		create an adult woman with an average body type, but still allow
		the program to randomly select her profession:
			character = Person(charType="human", age="adult", gender="female",
						bodyType="average")
		'''
		self.charType = charType
		self.profession = profession
		self.age = age
		self.gender = gender

	def __repr__(self):
		""" Method that helps python understand how to print a Person

		For example, you can now create a character in your code somewhere:
			character = Person()

		and then print that character to see what characteristics it has:
			print(character)
		"""
		if self.charType == "human":
			readable = '['
			if self.age:
				readable += self.age
			if self.gender:
				readable += ' ' + self.gender + ']'
			if self.profession:
				readable += ' job: ' + self.profession
		else:
			readable = self.charType
		return readable

# -------- END CLASS: Helper functions to randomly create characters ---------#

# The following variables not only contain the possibilities of different
# attributes of people/animals, but also the probability with which they
# appear. For example, charTypeS contains 'human' 4 times and 'animal'
# just 1 time. That means that 'human' is 4x more likely to appear.

# Choose between a human or animal
charTypeS = ["human", "human", "human", "animal", "human"]
# If it's an animal, choose between cat or dog
ANIMAL_TYPES = ["cat", "dog"]
# Possible ages of humans
AGE_TYPES = ["baby", "child", "adult", "adult", "adult", "elderly"]
# Possible professions of adults
PROF_TYPES = ["doctor", "CEO", "criminal", "programmer", "unemployed", "unknown", "unknown", "unknown"]
# Possible genders of humans
GENDER_TYPES = ["male", "female", "nonbinary"]

def create_random_person(charType=None, age=None, profession=None,
	  gender=None):
	# set type of character (human or animal?)
	if charType == None:
		charType = random.choice(charTypeS) # you is also a char type

	# If it's an animal, choose which type
	if charType == "animal":
		charType = random.choice(ANIMAL_TYPES)
	# If it's a character, set the characteristics
	if charType == "human":
		age = random.choice(AGE_TYPES)
		gender = random.choice(GENDER_TYPES)

		# Set adult characteristics.
		if age == "adult" and not profession:
			profession = random.choice(PROF_TYPES)

	return Person(charType, age, profession, gender)