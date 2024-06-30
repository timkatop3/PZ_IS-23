class Animal:
    """Base class for all animals."""

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def breathe(self):
        print(f"{self.name} is breathing.")

    def eat(self):
        print(f"{self.name} is eating.")


class Dog(Animal):
    """Class representing a dog."""

    def __init__(self, name, breed):
        super().__init__(name, "dog")
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")


class Cat(Animal):
    """Class representing a cat."""

    def __init__(self, name, breed):
        super().__init__(name, "cat")
        self.breed = breed

    def purr(self):
        print(f"{self.name} is purring.")


# Create an Animal object
animal1 = Animal("Rex", "dinosaur")

# Create a Dog object
dog1 = Dog("Max", "Labrador Retriever")

# Create a Cat object
cat1 = Cat("Whiskers", "Siamese")

# Call methods on each object
animal1.breathe()
animal1.eat()

dog1.bark()
dog1.breathe()  # Inherited method from Animal

cat1.purr()
cat1.eat()  # Inherited method from Animal
