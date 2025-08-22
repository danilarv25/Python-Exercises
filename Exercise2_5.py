talents = float(input("Enter talents:\n"))
pounds = float(input("Enter pounds:\n"))
lots = float(input("Enter lots:\n"))
talents = talents*20*32*13.3
pounds = pounds*32*13.3
lots = lots*13.3
weight = talents+pounds+lots
kg = weight//1000
kg = int(kg)
grams = weight-(kg*1000)
grams = round(grams, 2)
print("The weight in modern units:\n"+str(kg)+" kilograms and "+str(grams)+" grams.")