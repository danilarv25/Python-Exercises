class Dog:
    def __init__(self, name, birth_year, sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(self.name + " barks: " + self.sound)
        return

class Hotel:
    def __init__(self):
        self.dogs = []

    def dog_checkin(self, dog):
        self.dogs.append(dog)
        print(dog.name + " checked in")
        return

    def dog_checkout(self, dog):
        self.dogs.remove(dog)
        print(dog.name + " checked out")
        return

    def greet_dogs(self):
        for dog in self.dogs:
            dog.bark(1)

dog1 = Dog("Edina", 2014, "Hrmph!")
dog2 = Dog("Oreo", 2009, "Urruff!")
dog3 = Dog("Tiger", 2006)

hotel = Hotel()

hotel.dog_checkin(dog1)
hotel.dog_checkin(dog2)
hotel.dog_checkin(dog3)
hotel.greet_dogs()

hotel.dog_checkout(dog1)
hotel.greet_dogs()