def test1():
    print("call test1")
test1()

def test2(x,y,z):
    print(x,y,z)

test2(1,2,3)
test2(x=1,y=2,z=3)

def test3(x:int, y:str, z:bool):
    print(str(x), str(y), str(z))

test3(x=3, y="ok", z=True)

def test4(a:int,b:int):
    return a+b

print(test4(3,6))

def test5(a:int,b:int):
    return float(a+b), "ok"

data, result = test5(2,5)
print(data, result)