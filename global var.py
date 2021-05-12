tmp1 = "brothjs"


def change():
    tmp1 = "jsbroth"
    print("tmp1 in change function : " + tmp1)

def changeGlobal():
    global tmp1
    tmp1 = "jsbroth"
    print("tmp1 in changeGlobal function : " + tmp1)



print(tmp1)
change()
print(tmp1)

changeGlobal()
print(tmp1)
