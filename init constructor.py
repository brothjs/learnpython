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
        self.print()

    def print(self):
        print("from self : {}, {}".format(self.username, self.password))

# Create object from above class
user1 = User("Note", "test")
user2 = User()


