def test(*courses):
    print(courses[0])
test("KFC")

def test1(*course):
    print(course[1])
test1("KFC","Mc")

def test2(printAll:bool, *cause):
    if printAll:
        for c in cause:
            print(c)


test2(False,"KFC","Mc","CHESTER")