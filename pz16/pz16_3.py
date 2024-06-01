# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в
# бинарном формате.
import pickle

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f"Имя: {self.name}, Вид: {self.species}"

def save_def(animals, filename):
    with open(filename, 'wb') as f:
        pickle.dump(animals, f)

def load_def(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

animals = [
    Animal("Барсик", "Кошка"),
    Animal("Шарик", "Собака"),
    Animal("Кеша", "Попугай")
]

save_def(animals, 'pz16/animals.pkl')

loaded_animals = load_def('pz16/animals.pkl')

print(loaded_animals[0])
print(loaded_animals[1])
print(loaded_animals[2])