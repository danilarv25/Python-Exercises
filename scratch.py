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

