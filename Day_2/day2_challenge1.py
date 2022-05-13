# Get the user input
two_digit_number = input("Type a two digit number: ")


# Taking an input of a two-digit number, performing type manipulations, and printing the results.

two_digit_number_string = str(two_digit_number)  # converts the input to a string
digit_1_int = int(two_digit_number_string[0])  # new variable to take the string's first character and convert to int
digit_2_int = int(two_digit_number_string[1])  # same for second digit

# printing the results

print(two_digit_number_string[0] + " + " + two_digit_number_string[1] + " = " + str(digit_1_int+digit_2_int))
print(digit_1_int + digit_2_int)
