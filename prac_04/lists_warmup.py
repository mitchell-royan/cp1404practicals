"""
CP1404 - Practical 04
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] returns 3
# numbers[-1] returns 2
# numbers[3] returns 1
# numbers[:-1] returns [3, 1, 4, 1, 5, 9] as it slices the last number
# numbers[3:4] returns [1]
# 5 in numbers returns True
# 7 in numbers returns False
# numbers + [6, 5, 3] returns [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Change first element to the string ten
numbers[0] = "ten"

# Change last element to 1
numbers[-1] = 1

# Print all elements except first two
print(numbers[2:])

# Print whether 9 is an element of numbers
print(9 in numbers)







