class Elevator:
    def __init__(self, top:int, bottom=1):
        self.top = top
        self.bottom = bottom
        self.position = bottom

    def go_to_floor(self, floor:int):
        if floor < self.bottom or floor > self.top:
            print("That floor doesn't exist!")
        elif floor > self.position:
            move = floor - self.position
            for i in range(move):
                self.floor_up()
                print(f'Current floor: {self.position}')
        elif floor < self.position:
            move = self.position - floor
            for i in range(move):
                self.floor_down()
                print(f'Current floor: {self.position}')
        return

    def floor_up(self):
        self.position+=1

    def floor_down(self):
        self.position-=1

class Building:
    def __init__(self, top, elevators, bottom=1):
        self.top = top
        self.elevators = elevators
        self.bottom = bottom
        self.lifts = []
        for i in range(elevators):
            self.lifts.append(Elevator(self.top, self.bottom))

    def run_elevator(self, elevator_num, floor_destination):
        if elevator_num > len(self.lifts):
            print("That elevator doesn't exist!")
        else:
            self.lifts[elevator_num-1].go_to_floor(floor_destination)

    def fire_alarm(self):
        num = 1
        for i in self.lifts:
            print(f'\nFIRE ALARM!!! Sending elevator {num} down')
            i.go_to_floor(1)
            num += 1

b = Building(8,3)

print("Sending elevator 1 up")
b.run_elevator(1,4)
print("\nSending elevator 2 up")
b.run_elevator(2,6)
print("\nSending elevator 3 up")
b.run_elevator(3,8)

b.fire_alarm()

# print("\nSending elevator 1 down")
# b.run_elevator(1,1)
# print("\nSending elevator 2 down to non-existent floor (-1)")
# b.run_elevator(2,(-1))
# print("\nSending elevator 2 down")
# b.run_elevator(2,1)
# print("\nSending elevator 3 up to non-existent floor (9)")
# b.run_elevator(3,9)
# print("\nSending elevator 3 down")
# b.run_elevator(3,1)
# print("\nSending elevator non-existent elevator")
# b.run_elevator(4,4)