import random
import pandas as pd

class Car:
    def __init__(self, registration, max_speed,
                 current_speed = 0, travelled_distance = 0):

        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, kmh:int):
        if (self.current_speed + kmh) <= 0:
            self.current_speed = 0
        elif self.current_speed <= (self.max_speed - kmh):
            self.current_speed += kmh
        elif self.current_speed > (self.max_speed - kmh):
            self.current_speed = self.max_speed

    def drive(self, hours:float):
        self.travelled_distance += abs(self.current_speed)*hours

class Race:
    def __init__(self, name:str, km:int, racer_list):
        self.name = name
        self.km = km
        self.racer_list = racer_list

    def hour_passes(self):
        for i in self.racer_list:
            i.accelerate(random.randint(-10, 15))
            i.drive(1)

    def print_status(self):
        info = []
        for i in self.racer_list:
            racer = []
            racer.append(i.registration)
            racer.append(i.max_speed)
            racer.append(i.current_speed)
            racer.append(i.travelled_distance)
            info.append(racer)
        print(f"\n{self.name} stats:")
        df = pd.DataFrame(info, columns=['Registration', 'Max Speed', 'Current Speed', 'Travelled Distance'])
        print(df)

    def race_finished(self):
        for i in self.racer_list:
            if i.travelled_distance >= self.km:
                return True


cars = []
num = 1

for i in range(10):
    reg = "ABC-"+str(num)
    max = random.randint(100,200)
    cars.append(Car(reg, max))
    num+=1

print("Our racers:")
for i in cars:
    print(f"{i.registration} with a max speed of {i.max_speed} km/hr")

race = Race("Grand Demolition Derby", 8000, cars)

hour = 1
# not_racing = False
print("\nRacing...\n")
while not race.race_finished():
    race.hour_passes()
    hour += 1
    # not_racing = race.race_finished()
    if hour % 10 == 0:
        race.print_status()
print(f"\nHours passed: {hour}")
race.print_status()