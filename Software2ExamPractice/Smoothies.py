class Food:
    def __init__(self, name:str, calories:int):
        self.name = name
        self.calories = calories

    def info(self):
        print(f"{self.name} with {self.calories} calories")

class Fruit(Food):
    def __init__(self, name: str, calories: int, is_sweet:bool, type="fruit"):
        super().__init__(name, calories)
        self.is_sweet = is_sweet
        self.type = type

    def info(self):
        super().info()
        if self.is_sweet:
            print(f"    is sweet")
        else:
            print(f"    is not sweet")


class Vegetable(Food):
    def __init__(self, name: str, calories: int, is_leafy: bool, type = "vegetable"):
        super().__init__(name, calories)
        self.is_leafy = is_leafy
        self.type = type

    def info(self):
        super().info()
        if self.is_leafy:
            print(f"    is leafy")
        else:
            print(f"    is not leafy")

class Store:
    def __init__(self):
        self.inventory = dict()

    def add_item(self, food_object):
        self.inventory.update({food_object.name : food_object})

    def storage(self):
        print("We have...")
        for i in self.inventory:
            print(i)
            print(f"    {self.inventory[i].type}")
            print(f"    {self.inventory[i].calories} calories")
            if self.inventory[i].type == "vegetable":
                if self.inventory[i].is_leafy:
                    print(f"    leafy")
                else:
                    print(f"    not leafy")
            elif self.inventory[i].type == "fruit":
                if self.inventory[i].is_sweet:
                    print(f"    sweet")
                else:
                    print(f"    not sweet")
    def buy(self, product:str):
        if product in self.inventory.keys():
            print(f"purchased {product}")
            return self.inventory[product]
        else:
            print("Sorry, we don't sell that right now!")

class Kitchen:
    def __init__(self):
        self.pantry = []

    def grocery_run(self, store_object):
        gostore = input("Go to store? (y/n)")
        while gostore.lower() == "y":
            store_object.storage()
            product = input("What will you buy?")
            purchased = store_object.buy(product)
            if purchased:
                self.pantry.append(purchased)
            gostore = input("Continue shopping?")
        return gostore.lower()

    def make_smoothie(self):
        total_calories = 0
        ingredients = 0
        print("Pooring the entire pantry into one blender...")
        for i in self.pantry:
            ingredients += 1
            print(f"Adding {i.name}...")
            total_calories += i.calories

        for i in range(len(self.pantry)):
            self.pantry.pop()

        print("pantry empty")
        print("Done!")
        smoothie_info = "Smoothie with " + str(ingredients) + " ingredients and " + str(total_calories) + " calories"
        return smoothie_info



fru1 = Fruit("banana", 100, True)
fru2 = Fruit("orange", 80, True)
veg1 = Vegetable("carrot", 50, False)
store = Store()
kitchen = Kitchen()
store.add_item(fru1)
store.add_item(fru2)
store.add_item(veg1)
print("Added food items")

goon = "y"

while goon == "y":
    kitchen.grocery_run(store)
    my_smoothie = kitchen.make_smoothie()
    print(my_smoothie)
    goon = input("Go to store and make another smoothie? (y/n)")
