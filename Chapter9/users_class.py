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

user1 = User("John", "Smith", 18, "not enrolled")
user2 = User("Jerry", "Mcguire", 45, "enrolled")
user3 = User("Larry", "Collins", 21, "not enrolled")

user1.greetings()
user2.greetings()
user3.greetings()

user1.describe()
user2.describe()
user3.describe()
