#Создайте класс "Человек" с атрибутами "имя", "возраст" и "пол". Напишите метод,
#который выводит информацию о человеке в формате "Имя: имя, Возраст: возраст,
#Пол: пол".
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


# Create a Person object
person1 = Person("Иван Петров", 35, "мужчина")

# Display the person's information
person1.print_person_info()

