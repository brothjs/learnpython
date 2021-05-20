# Define class
class User:
    username = ""
    password = ""

    def __init__(self, username="admin",password="1234"):
        self.username = username
        self.password = password
#function ที่สร้างภายใน class จะต้องมี self หรือ argument ตัวแรกเสมอ
# เป็น object ที่แทนตัวคลาสของเรา ไม่งั้นอีกวิธี คือ static method
    @staticmethod
    def test():
        print("1234")


User.test()