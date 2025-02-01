mylist = [1, 2, 3]

myset = set()


class Dog:
    species = "mammal"  # Same for any instance of the class

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def bark(self, numbers):
        print("WOOF! My name is {} and the number is {}".format(self.name, numbers))


my_dog = Dog(breed="Huskie", name="Sammy")
my_dog2 = Dog(breed="Lab", name="Franky")

print(type(my_dog))

print(my_dog.species)
print(my_dog.breed, my_dog.name)

my_dog.bark(5)
my_dog2.bark(8)


class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    def get_circumference(self):
        return self.radius * Circle.pi * 2


my_circle = Circle()
my_circle2 = Circle(3)

print(my_circle.radius, "-", my_circle.get_circumference(), "-", my_circle.area)
print(my_circle2.radius, "-", my_circle2.get_circumference(), "-", my_circle2.area)
