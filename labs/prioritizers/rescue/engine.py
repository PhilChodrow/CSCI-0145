from rescue.scenario import Scenario

"""
The following set of exercises was developed by Vinesh Kanna (MimirHQ) based on an activity by Evan Peck (Bucknell University). It was modifed by Evan Peck to match a disaster-relief scenario.
"""

def ruleset1(scenario):
  """
  Decides whether your robot will save the people location 1 or location 2
  - Save the person in location 1, if and ONLY if they are not trespassing. Otherwise, save the person in location 2

  Note: in this activity, there will only be one person in each location
  @param scenario: details about the scenario
  @return: "people in loc1" or "people in loc2" depending on who you want to save
  """
  loc1person = scenario.loc1people[0]
  
  loc2person = scenario.loc2people[0]
  # TODO: Fill in the method
  return "people in loc1"


def ruleset2(scenario):
  """
  Decides whether your robot will save the people location 1 or location 2
  - Save the person in location 2, if they are NOT trespassing or if they are a child.

  Note: in this activity, there will only be one person in each location
  @param scenario: details about the scenario
  @return: "people in loc1" or "people in loc2" depending on who you want to save
  """
  loc1person = scenario.loc1people[0]
  loc2person = scenario.loc2people[0]
  # TODO: Fill in the method
  return "people in loc1"


def ruleset3(scenario):
  """
  Decides whether your robot will save the people location 1 or location 2
  - The first priority is to save the person who is a baby.
  - The second priority is to save athletic people.
  - The third priority is to save people who are either a doctor or a CEO.
  - The fourth priority is to save females.
  - The fifth priority is to save the loc1person.

  Note: in this activity, there will only be one person in each location
  @param scenario: details about the scenario
  @return: "people in loc1" or "people in loc2" depending on who you want to save
  """
  loc1person = scenario.loc1people[0]
  loc2person = scenario.loc2people[0]
  # TODO: Fill in the method
  return "people in loc1"


def our_ruleset(scenario):
  """
  Decides whether your robot will save the people location 1 or location 2
  - Your own decision algorithm.

  Note: in this activity, there will only be one person in each location
  @param scenario: details about the scenario
  @return: "people in loc1" or "people in loc2" depending on who you want to save
  """
  loc1person = scenario.loc1people[0]
  loc2person = scenario.loc2people[0]
  # TODO: Fill in the method
  return "people in loc1"

def group_decision(scenario):
  """
  Decides whether your robot will save the GROUP of people at location 1 or location 2
  - Your own decision algorithm.

  Note: in this activity, there will be 1 to 4 people in each location
  @param scenario: details about the scenario
  @return: "people in loc1" or "people in loc2" depending on who you want to save
  """
  loc1people = scenario.loc1people
  loc2people = scenario.loc2people
  # TODO: Fill in the method
  return "people in loc1"