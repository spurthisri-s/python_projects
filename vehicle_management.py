class Vehicle:

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Vehicle:", self.name)


class Car(Vehicle):

    def speed(self):
        print("Speed: 120 km/h")


class Bike(Vehicle):

    def speed(self):
        print("Speed: 80 km/h")


car = Car("Honda City")
bike = Bike("Royal Enfield")

car.show()
car.speed()

print()

bike.show()
bike.speed()