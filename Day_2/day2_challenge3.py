# calculator program to reveal how much life you have left in years, months, weeks, and days

# receiving the user's age as an input

age = input("What is your current age?")

# converting the input to an integer, and then into various lengths of time

years_left = 90 - int(age)
months_left = round(years_left * 12)
weeks_left = round(years_left * 52)
days_left = round(years_left * 365)

# creating a string message and printing

message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print(message)
