class User:
    def __init__(self, first_name, last_name, age, enrollment):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.enrollment = enrollment

    def greetings(self):
        print(f"Hello {self.first_name} {self.last_name}")
    
    def describe(self):
        print(f"The user {self.first_name} {self.last_name} is {self.age} and is {self.enrollment} at NMC")
