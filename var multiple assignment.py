#pack
def getData():
    return 0,1,2
x = y = z = 0
x1, y1, z1 = 0,1,2
x2,y2,z2 = getData()
print(x,y,z)
print(x1,y1,z1)
print(x2,y2,z2)

#unpack
courses = ["Angular", "Python", "React"]
angularTitle, pythonTitle, reactTitle = courses
print(angularTitle,pythonTitle,reactTitle)
print(courses)