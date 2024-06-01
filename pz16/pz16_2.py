# Создайте класс "Фигура", который содержит метод расчета площади фигуры.
# Создайте классы "Квадрат" и "Прямоугольник", которые наследуются от класса
# "Фигура". Каждый класс должен иметь метод расчета площади собственной фигуры.
class Figure():
    def __init__(self, height, width):
        pass

    def calculate(self):
        pass    

class Rectangle(Figure):
    def __init__(self, height, width):
            self.height = height
            self.width = width

    def calculate(self):
        return self.width * self.height

class Squar(Figure):
    def __init__(self, side):
        self.side = side

    def calculate(self):
        return self.side * self.side

rectangle = Rectangle(12, 21)
print(rectangle.calculate()) 

sqar = Squar(2)
print(sqar.calculate())