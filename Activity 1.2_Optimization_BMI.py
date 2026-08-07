def isfloat(n):
  """ 
  If string can be converted to floating number 
  returns that number, otherwise returns false
  """
  try:
    n=float(n)
    return n;
  except ValueError:
     return False;

def inputfloat(hint):
  """ 
  Prints hint and asks to enter number.
  Repeats until decimal number is entered.
  """
  ret = False
  while ret is False:
    ret = isfloat(input(hint))
    if ret is False:
      print("Please enter number")
  return ret 


class BMIcalculator:
    def __init__(self):
        self.w = 0
        self.h = 0

    def getdata(self):
        self.w = inputfloat("Enter your weight in kilograms: ")
        self.h = inputfloat("Enter your height in centimeters: ")

    def calculate(self):
        return round(self.w / (self.h * self.h), 2)


def main():
  print("\n","="*42,"\n")
  print("Hello, let's calculate your BMI.");
  
  calc = BMIcalculator()
  print()
  calc.getdata()
  bmi=calc.calculate()
  print(f"Your BMI is {bmi}")
  print("\n","="*42,"\n")

if __name__ == "__main__":
    main()