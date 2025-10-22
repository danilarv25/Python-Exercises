"""THIS CODE SOLVES TASKS 1, 2, and 3 of MODULE 9"""

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


car0 = Car("ABC-123", 142)

print(f"""Registration number: {car0.registration}  
Max speed: {car0.max_speed} km/h
Current speed: {car0.current_speed} km/h 
Travelled: {car0.travelled_distance} km\n""")

car0.accelerate(30)
car0.drive(0.5)
car0.accelerate(70)
car0.drive(2)
car0.accelerate(50)
car0.drive(1)
print(f"""Registration number: {car0.registration}  
Max speed: {car0.max_speed} km/h
Current speed: {car0.current_speed} km/h 
Travelled: {car0.travelled_distance} km\n""")

car0.accelerate(-200)
print(f"""Registration number: {car0.registration}  
Max speed: {car0.max_speed} km/h
Current speed: {car0.current_speed} km/h 
Travelled: {car0.travelled_distance} km\n""")