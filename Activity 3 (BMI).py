
# This program calculates the Body Mass Index (BMI) based on user input for weight and height.

# Prompt the user to enter their weight in kilograms and height in centimeters
class BMI_Calculator:
    def get_user_input(self):
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in centimeters: "))
        return weight, height
# Calculate BMI using the formula: BMI = weight (kg) / (height (m))^2
    def calculate_bmi(self, weight, height):
        return weight / (height * height) * 10000
# Determine the BMI category based on the calculated BMI value
    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi <= 24.9:
            return "Normal weight"
        elif 25 <= bmi <= 29.9:
            return "Overweight"
        else:
            return "Obese"
# Main function to run the BMI calculator
if __name__ == "__main__":
    calculator = BMI_Calculator()
    weight, height = calculator.get_user_input()
    bmi = calculator.calculate_bmi(weight, height)
    category = calculator.get_bmi_category(bmi)
    print(f"Your BMI is {bmi:.1f}")
    print(f"You are {category}.")