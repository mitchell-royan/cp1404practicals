import random

print(random.randint(5, 20))  # line 1
# The smallest number that could have been seen is 5 with the largest being 20.

print(random.randrange(3, 10, 2))  # line 2
# Smallest number that could be seen is 3, with the largest being 9.
# Line 2 could not have produced a 4, this is due to the step size being a 2 and as it starts at 3 the next step is 5.

print(random.uniform(2.5, 5.5))  # line 3
# The smallest number that could be seen is 2.5 whereas the largest is 5.5

print(random.randint(1, 100))  # Random number between 1 and 100 inclusive
