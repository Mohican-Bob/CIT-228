from user import User
from priveleges import Priveleges
from admin import Admin


priv = ["can add post", "can delete post", "can ban user"]

priveleges = Priveleges(priv)
user1 = User("John", "Smith", 18, "not enrolled")
user2 = User("Jerry", "Mcguire", 45, "enrolled")
user3 = User("Larry", "Collins", 21, "not enrolled")
admin1 = Admin("Shiane", "Stone", 46, "enrolled", priveleges)



user1.greetings()
user2.greetings()
user3.greetings()
admin1.greetings()

user1.describe()
user2.describe()
user3.describe()
admin1.describe()
priveleges.show_priveleges()