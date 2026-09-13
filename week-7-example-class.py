class GrandFather:
    def __init__ (self, grandFatherName):
        self.grandFatherName = grandFatherName

class Father(GrandFather):
    def __init__ (self, FatherName, grandFatherName):
            self.FatherName = FatherName
            super().__init__(grandFatherName)

class Son(Father):
    def __init__ (self, SonName, FatherName, grandFatherName):
         self.sonName = SonName
         super().__init__(FatherName, grandFatherName)

    def display(self):
         print(f"Son: {self.sonName}")
         print(f"Father: {self.FatherName}")
         print(f"Grand Father: {self.grandFatherName}")

s1 = Son("Jack", "Bob", "William")
s1.display()