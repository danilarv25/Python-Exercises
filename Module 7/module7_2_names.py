nms = set()

while True:
    name = input("Write a name (empty string to quit): ")
    if name == "":
        break
    if name in nms:
        print("Existing name")
    else:
        print("New name")
        nms.add(name)

for i in nms:
    print(i)