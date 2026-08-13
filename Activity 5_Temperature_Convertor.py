
#Create a class called TemperatureConverter that has a method called convert.
class TemperatureConverter:
    
#define the convert method that takes a temperature string as input and converts it to the other unit.
    def convert(self, temperature):
        unit = temperature[0]
        value = float(temperature[1:])
#Create a conditional statement that checks the unit of the temperature and performs the conversion.
        if unit == "F":
            celsius = (value - 32) * 5 / 9
            return f"{value:g} degrees Fahrenheit is converted to {celsius:.2f} degrees Celsius"

        elif unit == "C":
            fahrenheit = (value * 9 / 5) + 32
            return f"{value:g} degrees Celsius is converted to {fahrenheit:.2f} degrees Fahrenheit"

        else:
            return "Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix."

#Create an instance of the TemperatureConverter class and prompt the user to enter a temperature in either Farenheit or Celsius.
converter = TemperatureConverter()

temperature = input("Enter temperature (e.g. F51 or C11): ")

print(converter.convert(temperature))