class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def sound(self):
        print(f'Sound!')

    def print_info(self):
        print(f'My name is {self.name} and I am a {self.species}')

class Lion(Animal):
    def __init__(self, name, species = "Lion"):
        super().__init__(name, species)

    def sound(self):
        print(f'Roar!')

    def print_info(self):
        print(f'My name is {self.name} and I am a {self.species}')

class Elephant(Animal):
    def __init__(self, name, species = "Elephant"):
        super().__init__(name, species)

    def sound(self):
        print(f'Troooot!')

    def print_info(self):
        print(f'My name is {self.name} and I am a {self.species}')

class Snake(Animal):
    def __init__(self, name, species = "Snake"):
        super().__init__(name, species)

    def sound(self):
        print(f'Hissss!')

    def print_info(self):
        print(f'My name is {self.name} and I am a {self.species}')

class Zoo:
    def __init__(self):
        self.all_animals = []

    def add_animal(self, animal):
        self.all_animals.append(animal)

    def show_animals(self):
        for a in self.all_animals:
            a.print_info()

    def all_sounds(self):
        for a in self.all_animals:
            a.sound()

place = Zoo()
lion1 = Lion("Bob")
eleph = Elephant("Earnie")
snek = Snake("Frank")
place.add_animal(lion1)
place.add_animal(eleph)
place.add_animal(snek)
place.show_animals()
place.all_sounds()