import inspect


class Pet:
    def __init__(self, name, breed, date_of_birth):
        self.name = name
        self.breed = breed
        self.date_of_birth = date_of_birth

    def personal_data(self):
        print(f'Имя питомца: {self.name()}.\n Порода: {self.breed}.\n Дата рождения: {self.date_of_birth}')


def introspection_info(obj):
    a1 = type(obj)
    a2 = hasattr(obj, 'name')
    a3 = dir(obj)[0:3]
    a4 = inspect.getmodule(obj)
    if isinstance(obj, type(obj)):
        print('Не может не принадлежать')
    a5 = inspect.isfunction(obj)
    return {'type': a1, 'attributes': a2, 'methods': a3, 'module': a4, 'func?': a5}


my_pet = Pet('Марсель', 'Бигль', '16.07.2022')
number_info = introspection_info(my_pet)
print(number_info)
