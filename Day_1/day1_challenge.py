# Variables challenge - swapping the stored values of the two variables 'a' and 'b'

a = input("a: ")  # using user input to store 'a'
b = input("b: ")  # using user input to store 'b'

# The following block introduces a new variable, 'c' to perform the swap

c = b  # c copies the data from b
b = a  # b replaces its data from a
a = c  # a replaces its data from c

# Printing the results, showing the completed swap.

print("a: " + a)
print("b: " + b)
