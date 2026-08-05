
# This program calculates the Body Mass Index (BMI) based on user input for weight and height.
if __name__ == "__main__":

# Prompt the user to enter their weight in kilograms and height in centimeters
    weight = float(input("Enter your weight in Kilograms: "))
    height = float(input("Enter your height in Centimeters: "))

# Calculate BMI using the formula: BMI = weight (kg) / (height(cm) * height(cm) * 10000
    bmi = float(weight / (height * height) * 10000)
    if bmi < 18.5:
       print("You are Underweight.")  
    elif bmi >= 18.5 and bmi <= 24.9:
        print("You have a normal weight.")
    elif bmi >= 25 and bmi <= 29.9:
         print("You are Overweight.")
    else:
        print("You are Obese.")