def no_evens(list):
    newlist = []
    for i in list:
        newlist.append(i)
    for i in newlist:
        if i % 2 == 0:
            newlist.remove(i)
    return newlist

list = [1,2,3,4,5,6]
oddlist = no_evens(list)
print(list)
print(oddlist)