class Car:
    def __init__(self, brand, color, mileage = 0, fuel = 100):
        self.brand = brand
        self.color = color
        self.mileage = mileage
        self.fuel = fuel

    def drive(self, distance):
        if distance*0.5 > self.fuel:
            print(f"There is not enough fuel to drive {distance} km!")
        else:
            self.fuel -= distance*0.5
            position = self.mileage + distance
            print(f"The {self.color} {self.brand} is driving {distance} km, reaching {position} km")
            self.mileage += distance

    def repaint(self, new_color):
        self.color = new_color
        print(f"The {self.brand} has been painted {self.color}")

car1 = Car("Toyota", "blue")
car2 = Car("Subaru", "gray")

car1.drive(10)
car1.drive(7)
car1.repaint("red")
car1.drive(2)
print(car1.fuel)
car2.drive(15)
car2.repaint("rainbow")
car2.drive(50)
print(car2.fuel)
car2.drive(140)

