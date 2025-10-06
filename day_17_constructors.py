# python day_17_constructors.py

"""class Animal:
    # This code will fail as muliple constructors are not allowed in Python (but we can do with hack)
    def __init__(self,name,species):
        self.name=name
        self.species=species

    # It will only use this constructor
    def __init__(self,name,species,age):
        self.name=name
        self.species=species
        self.age=age

    def make_sound(self,sound):
        return "The animal is {} and says {}".format(self.name,sound)

dog =Animal("dog","Mammals")
print(dog)"""

# Now it will run with 3 arguments
"""class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    
    def __init__(self,name,species,age):
        self.name=name
        self.species=species
        self.age=age

    def make_sound(self,sound):
        return "The animal is {} and says {}".format(self.name,sound)

dog =Animal("dog","Mammals",17)
print(dog)"""


# We can use multiple constructors using *args
class Animal:
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.species = args[1]
        elif len(args) == 3:
            self.name = args[0]
            self.species = args[1]
            self.age = args[2]

    def make_sound(self, sound):
        return "The animal is {} and says {}".format(self.name, sound)


dog = Animal("Mogli", "mammals")
print(dog.name)
print(dog.species)
print(dog.make_sound("woof wwoof"))
