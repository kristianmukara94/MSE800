class UniversityConfig:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
  
            cls._instance.university_name = ""
            cls._instance.academic_year = ""
            cls._instance.semester = ""
            cls._instance._instance = True
        return cls._instance

    def set_config(self, university_name: str, academic_year: str, semester: str):
        self.university_name = university_name
        self.academic_year = academic_year
        self.semester = semester

    def display_config(self):
        print("University Config")
        print(f"University Name: {self.university_name}")
        print(f"Academic Year: {self.academic_year}")
        print(f"Semester: {self.semester}")


config1 = UniversityConfig()
config2 = UniversityConfig()
config3 = UniversityConfig()


config1.set_config(
    university_name="Yoobee",
    academic_year="2026-2027",
    semester="Semester 1"
)


print("Displaying config via config2:")
config2.display_config()

print("Instance identity verification:")
print(f"config1 is config2: {config1 is config2}")
print(f"config2 is config3: {config2 is config3}")
print(f"config1 is config3: {config1 is config3}")

print(f"\nMemory address of config1 {hex(id(config1))}")
print(f"memory address of config2 {hex(id(config2))}")
print(f"Memory address of config3 {hex(id(config3))}")