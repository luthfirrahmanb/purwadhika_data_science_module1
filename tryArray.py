arrayNum = [100, 1, 3, 20, 15, 75, 4]
newArray = []

while arrayNum:
    minimumNumber = arrayNum[0]
    for x in arrayNum:
        if(x < minimumNumber):
            minimumNumber = x
    newArray.append(minimumNumber)
    arrayNum.remove(minimumNumber)

print(newArray)

testList = [1, 2, 3]
newList = testList.copy()

newList[1] = "maman"
print(testList)
print(newList)