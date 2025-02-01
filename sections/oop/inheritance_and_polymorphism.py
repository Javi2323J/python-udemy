class Animal:
    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


myanimal = Animal()
myanimal.who_am_i()
myanimal.eat()


class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog Created")

    def eat(self):
        print("I am eating")

    def bark(self):
        print("WOOF!")


mydog = Dog()
mydog.who_am_i()
mydog.eat()
mydog.bark()

# POLYMORPHISM
print("\nPOLYMORPHISM\n")


class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"


niko = Dog("niko")
felix = Cat("felix")

print(niko.speak())
print(felix.speak())

for pet_class in [niko, felix]:
    print(type(pet_class))
    print(pet_class.speak())


def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


# myanimal = Animal("Fred")
# myanimal.speak()


class Dog(Animal):
    def speak(self):
        return self.name + " says woof!"


class Cat(Animal):
    def speak(self):
        return self.name + " says meow!"


fido = Dog("Fido")
isis = Cat("Isis")

print(fido.speak())
print(isis.speak())
