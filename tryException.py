# Define Class
class Calculator:

    def divide(self, a, b):
        return a/b

c =Calculator()

try:
    print(c.divide(1,3))
    dataArray = [0,1,2]
    print(dataArray[3])

except ZeroDivisionError:
    print("zero division error")
except IndexError:
    print("index out of boundary")
except :
    print("invalid data")
