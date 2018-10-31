

# Print out the Python path
import sys
print(sys.path)

# Get number of characters
import string
print(len(string.ascii_letters))

# Get a random letter
import random
print(random.choice(string.ascii_letters))

# Create a six digit code
print(help(random.sample))
print(random.sample(string.ascii_letters, 6))