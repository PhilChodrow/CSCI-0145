
from rescue.scenario import (
  set_seed,
  Scenario,
  create_random_scenario
)

from rescue.engine import (
  ruleset1,
  ruleset2,
  ruleset3,
  our_ruleset,
  group_decision
)

def run_simulation(ruleset = ruleset1, **kwargs):
  """
  run a simulation by generating a random scenario and applying a user-specified ruleset to decide between rescuing the people in loc1 or the people in loc2. 
  """
  print("===========================================")
  print("THE ETHICAL ENGINE")
  print("===========================================")
  print()

  # If you want to continually test the same scenario
  # instead of one that is truly random, uncomment
  # the line below so that your program starts 
  # with the same set of people each time. 
  # set_seed(42)

  while True:
    scene = create_random_scenario(**kwargs)
    print(scene)
    print()
    result = ruleset(scene)
    print()
    input('Hit any key to see decision: ')
    print('I choose to save the', result + ".")
    print()

    # For breaking the loop
    response = input("Hit 'q' to quit or 'enter' to continue: ")
    if response == 'q':
      break

  print('Done')