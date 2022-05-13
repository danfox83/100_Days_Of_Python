# Goal is to create a simple bmi calculator

# Collecting the user inputs

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# calculations for bmi using new variables to convert inputs to floats

height_float = float(height)
weight_float = float(weight)
bmi = round((weight_float / (height_float ** 2)))

# series of if, elif, and else to print and describe results
# introduction to f strings

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, your weight is normal.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese")
