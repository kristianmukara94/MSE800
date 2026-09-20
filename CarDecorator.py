class car:
   def cost(self):
      return 25,000

   def description(self):
      return "Basic Car"

class CarDecorator:
      def __init__ (self, car):
         self.car = car

      def cost(self):
         return self.cost()


class GPSDecorator(CarDecorator):
      def cost(self):
          return self.cost() + 500

class SunroofDecorator(CarDecorator):
      def cost(self):
          return self.cost() + 1000

class Leather_SeatsDecorator(CarDecorator):
      def cost(self):
          return self.cost() + 1500

class Premium_Sound_System(CarDecorator):
      def cost(self):
          return self.cost() + 800

Car = car()
Car = GPSDecorator(car)
Car = SunroofDecorator(car)
Car = Leather_SeatsDecorator(car)
Car = Premium_Sound_System(car)

Car = GPSDecorator(SunroofDecorator(Leather_SeatsDecorator(Premium_Sound_System)))
print(car.cost)

   