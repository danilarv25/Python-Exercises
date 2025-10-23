import random

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

cars = {}
num = 1

for i in range(10):
    name = "Racer "+str(num)
    reg = "ABC-"+str(num)
    max = random.randint(100,200)
    cars[name] = Car(reg, max)
    #cars.append(Car(reg, max))
    num+=1

print("Our racers:")
for i in cars:
    print(f"{cars[i].registration} with a max speed of {cars[i].max_speed} km/hr")

print("\nRacing...\n")
racing = True
while racing:
    for i in cars:
        cars[i].accelerate(random.randint(-10,15))
        cars[i].drive(1)
        if cars[i].travelled_distance >= 10000:
            print(f"{cars[i].registration} has won!")
            print(f"""Their stats:
Max speed: {cars[i].max_speed} km/h
Current speed: {cars[i].current_speed} km/h 
Travelled: {cars[i].travelled_distance} km\n"""
)
            racing = False

# Creating the leaderboard
end = {}
leaderboard = {}
scorespot = 0
for i in cars:
    end[cars[i].registration] = cars[i].travelled_distance

print("THE LEADERBOARD\n")

scores = list(end.values())
scores.sort(reverse=True)

while len(leaderboard) < 10:
    for i in end:
        if end[i] == scores[scorespot]:
            print(f"{i} : {end[i]}")
            leaderboard[i] = end[i]
            scorespot+=1

# for i in leaderboard:
#     print(f"{i} : {leaderboard[i]}")

# for i in end:
#     print(f"{i} : {end[i]}")
