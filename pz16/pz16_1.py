# . Создайте класс "Животное" с атрибутами "имя" и "вид". Напишите метод, который
# выводит информацию о животном в формате "Имя: имя, Вид: вид".
class Animal():

    def __init__(self,name,view):
        self.name = name
        self.view = view

    def conclusion(self):
        print(f'Имя: {self.name}, вид: {self.view}')

animal = Animal('Черчель', 'жук')
animal.conclusion()
