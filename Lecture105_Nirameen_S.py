class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Pickup(Vehicle):
    pass;

class Car(Vehicle):
    pass;

class Van(Vehicle):
    pass;

class EstateCar(Vehicle):
    pass;

pickup1 = Pickup()
pickup1.turnOnAirConditioner()

car1 = Car()
car1.turnOnAirConditioner()

van1 = Van()
van1.turnOnAirConditioner()

estatecar1 = EstateCar()
estatecar1.turnOnAirConditioner()