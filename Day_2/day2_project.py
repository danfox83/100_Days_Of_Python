# tip calculator project

# welcome screen

print("Welcome to the tip calculator")

# inputs for the bill total, number of guests to split the bill, and the tip you want to leave

total_bill = float(input("What was the total bill? $"))
num_guests = int(input("How many guests will split the bill? "))
tip_percent = int(input("What percent tip (15, 18, 20) will you leave? "))

# calculations

total_with_tip = total_bill + (total_bill * tip_percent/100)
total_pp = round(total_with_tip/num_guests, 2)

# creating the message output and printing

message = f"Each of the {num_guests} guests should pay ${total_pp}"

print(message)
