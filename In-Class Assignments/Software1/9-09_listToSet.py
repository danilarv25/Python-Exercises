def uniqueNumbers(numbersList):
    newset = set()
    for i in numbersList:
        newset.add(i)
    return newset
def setLength(list):
    return len(set(list))

numList = [1,1,3,5,5,6]
numSet = uniqueNumbers(numList)
print(numSet)
print(len(numSet))
print(setLength(numList))
