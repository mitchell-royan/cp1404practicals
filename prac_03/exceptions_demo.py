"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
- ValueError will occur when something other than an integer is entered, like a word.

2. When will a ZeroDivisionError occur?
- When 0 is entered for the denominator, as this is not mathematically possible.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
- Yes, by checking that the denominator is not 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
