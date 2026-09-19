class Pizza:
 def Prepare (self):
  print("Pizza")

class Burger:
 def Prepare (self):
  print("Burger")

class Pasta:
  def Prepare (self):
   print("Pasta")

class RestaurantFactory:
 @staticmethod
 def order_type(OrderType):
  if OrderType == "Pizza":
   return Pizza()
  elif OrderType == "Burger":
   return Burger()
  elif OrderType == "Pasta":
   return Pasta()
  else:
   raise ValueError("Unknown order")
 
order = RestaurantFactory.order_type("Pizza")
order.Prepare()

 
 