# Define Class
class User:
    username = ""
    password = ""
#   กำหนดค่าเริ่มต้นให้ class user      
    """def __init__(self):
        self.username = "admin"
        self.password ="1234"
        self.print()
    """
    def __init__(self, username = "admin", password = "1234"):
        self.username = username
        self.password = password 
#  Inheritance / subclass
class UserV1(User):
    def clear(self):
        self.username = ""
        self.password = ""
    def __str__(self):
        return "username: {}, password: {}".format(self.username, self.password)


user1 = UserV1("Note", "test")
user1.clear()
print(user1)


