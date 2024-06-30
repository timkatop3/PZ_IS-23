import pickle

class Person:
    """Class to represent a person with attributes and a method to display information."""

    def __init__(self, name, age, gender):
        """Initialize the person's attributes."""
        self.name = name
        self.age = age
        self.gender = gender

    def print_person_info(self):
        """Display the person's information in a formatted way."""
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Пол: {self.gender}")


def save_def(persons, filename):
    """Saves a list of Person objects to a file using pickle."""
    with open(filename, "wb") as file:
        pickle.dump(persons, file)


def load_def(filename):
    """Loads a list of Person objects from a file using pickle."""
    with open(filename, "rb") as file:
        loaded_persons = pickle.load(file)
    return loaded_persons


# Create Person objects
person1 = Person("Иван Петров", 35, "мужчина")
person2 = Person("Мария Иванова", 28, "женщина")
person3 = Person("Сергей Кузнецов", 42, "мужчина")

persons_list = [person1, person2, person3]

# Save the list of Person objects to a file
save_def(persons_list, "persons.pickle")

# Load the list of Person objects from the file
loaded_persons = load_def("persons.pickle")

# Print the information of the loaded Person objects
for person in loaded_persons:
    person.print_person_info()
