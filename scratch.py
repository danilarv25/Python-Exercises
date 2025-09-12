import random

'''Buying lattes'''
# while True:
#     money = float(input("How much money you got?\n"))
#     if money < 0:
#         print("Negative money? What, you owe something? Pay up!")
#     elif money == 0:
#         print("Hah! You're broke, bud.")
#     elif 0 < money < 5:
#         print("Eh, not enough for a latte. Sorry, bud.")
#     else:
#         if money == 5:
#             print("Alright! One latte coming right up!")
#         elif 5 < money < 10:
#             lattes = money//5
#             change = money%5
#             print("Alright! "+str(int(lattes))+" latte coming right up! Your change is "+str(change)+".")
#         elif money >= 10:
#             lattes = money//5
#             change = money%5
#             print("Alright! "+str(int(lattes))+" lattes coming right up! Your change is "+str(change)+".")
#         break


'''How many rolls for two 6s'''
# rounds = totalrolls = 0
# while rounds < 100000:
#     rolls = d1 = d2 = 0
#     while (d1 != 6 or d2 != 6):
#         d1 = random.randint(1,6)
#         d2 = random.randint(1, 6)
#         rolls += 1
#     totalrolls += rolls
#     rounds += 1
# avg = totalrolls/1000
# print(f"On average, it took {avg:.2f} rolls to get two sixes.")

'''Sum function'''
# def sumxy(num1, num2):
#     result = x + y
#     print(result)
#     return
# x = int(input("x: "))
# y = int(input("y: "))
# sumxy(x,y)

'''List storing'''
# def makeList():
#     list = []
#     x = input("What item? (0 to quit): ")
#     while x != "0":
#         list.append(x)
#         x = input("What item? (0 to stop listing): ")
#     return list
#
# def storeList(dict, list):
#     newdict = {}
#     newdict.update(dict)
#     name = input("Name list: ")
#     newdict.update({name: list})
#     return newdict
#
# def listMain():
#     dict = {}
#     x = "y"
#     while x != "n":
#         newlist = makeList()
#         dict = storeList(dict, newlist)
#         x = input("Continue? y or n: ")
#     for i in dict:
#         print(i + "    " + str(dict[i]))
#     return dict
# dictStorage = {}
# task = int(input("Do task? (1) for yes, (0) for no:"))
# while task != 0:
#     task = int(input("What do you want to do?\n(1) Make a list\n: "))
#     if task == 1:
#         dictStorage.update(listMain())
#
# print(dictStorage)
## oldict = {}
## x = "y"
## while x !="n":
##     newlist = makeList()
##     oldict = storeList(oldict, newlist)
##     x = input("Continue? y or n: ")
#
## print()