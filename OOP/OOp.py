class Auto:
    def __init__(self, tyres, wheels, doors, seats, color):
        self.tyres = tyres
        self.wheels = wheels
        self.doors = doors
        self.seats = seats
        self.color = color
        self.my_data = range(1,30)

    def __len__(self):
        return len(self.my_data)

auto = Auto()
BMW = Auto(tyres=4, wheels=2, doors=4, seats=5, color="red")
audi = Auto(tyres=4, wheels=2, doors=4, seats=5, color="white")

print(len(auto.my_data))

class Driver:
    def drive_safe(self):
        print("Driving safe")

class Auto:
    pass

