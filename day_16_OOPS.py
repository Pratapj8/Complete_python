# python day_16_OOPS.py

# Classes - Object details
# constructors, attributes,methods

# why we use - code re-usability , code maintanability , modular coding

# Classes--Real world Entity or object , material (BMW Car) / blue print
# attributes ,features,properties --properties of the class (door , windows)
# methods ,functions --actions of the class(drive, self-driving)


# bad way to write
class car:
    pass


car_1 = car()
car_2 = car()

car_1.windows = 4
car_1.tyres = 4
car_1.engine = "diesel"
car_1.seats = 6

car_2.windows = 6
car_2.tyres = 6
car_2.engine = "petrol"


print(car_1)
print(car_1.engine)
print(car_1.windows)
print(car_2.engine)

# print(dir(car_1))



# Good Practice
# init nothing but constructor


class car:
    # constructor
    def __init__(self, windows, tyres, engine):
        self.windows = windows
        self.tyres = tyres
        self.engine = engine


car1 = car(4, 4, "petrol")
print("The no of tyres in object car1 is {}".format(car1.tyres))
print("The no of windows in object car1 is {}".format(car1.windows))


# More functions


class Car:
    # constructor
    def __init__(self, windows, tyres, engine):
        self.windows = windows
        self.tyres = tyres
        self.engine = engine

# This is method in car
    def self_driving(self, engine):
        print("The car type is {} engine ".format(engine))


car1 = Car(4, 4, "petrol")
print("The no of tyres in object car1 is {}".format(car1.tyres))
print("The no of windows in object car1 is {}".format(car1.windows))
car1.self_driving("electric")
