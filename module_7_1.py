from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        pprint(file.read())
        return file.close() and self.__file_name

    def add(self, *products):
        n = Shop.get_products(self)
        for i in products:
            if isinstance(i, Product):
                if i not in n:
                    file = open(self.__file_name, 'a')
                    file.seek(0)
                    file.write(f'{i} \n')
                    file.close()
                else:
                    file = open(self.__file_name, 'a', encoding='utf-8')
                    file.seek(0)
                    file.write(f'Продукт {i} уже есть в магазине\n')
                    file.close()
                    return self.__file_name


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
