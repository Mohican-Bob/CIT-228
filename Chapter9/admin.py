from user import User
from priveleges import Priveleges

class Admin(User):
    def __init__(self, first_name, last_name, age, enrollment, permissions):
        super().__init__(first_name, last_name, age, enrollment)
        self.priveleges = Priveleges(permissions)