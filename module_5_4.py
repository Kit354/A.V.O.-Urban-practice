class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        cls.houses_history.append(args[0])
        return obj

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for floor in range(1, new_floor + 1):
            if floor <= self.number_of_floors:
                print(floor)
            elif floor > self.number_of_floors or floor < 1:
                print('Такого этажа не существует')
                return

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
            return self
        elif isinstance(value, int):
            self.number_of_floors += value
            return self

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)

    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
