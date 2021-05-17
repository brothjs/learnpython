dictionaryData = {"ant":"มด","bee":"ผึ้ง",}
print(dictionaryData)
print(dictionaryData["ant"])
print(dictionaryData.get("bee"))
print(dictionaryData.keys())
dictionaryData["cat"] = "แมว"
print(dictionaryData)
dictionaryData.pop("bee")
print(dictionaryData)
del dictionaryData["ant"]
print(dictionaryData)