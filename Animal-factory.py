class Dog:
 def speak(self):
   print("Woof!")
class Cat:
 def speak(self):
   print("Meow")
class Cow:
 def speak(self):
   print("Moo!")
#Factory
class AnimalFactory:
 @staticmethod
 def create_animal(animal_type):
  if animal_type == "dog":
   return Dog()
  elif animal_type == "cat":
   return Cat()
  elif animal_type == "cow":
    return Cow()
  else:
   raise ValueError("Unknown animal")
animal = AnimalFactory.create_animal("dog")
animal.speak()