class Figure:
    sides_count = 0

    def __init__(self, __sides, __color, filled=True):
        self.__sides = [*__sides]
        self.__color = [__color]
        self.filed = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r and g and b, (int, float)):
            if 255 > r and g and b > 0:
                return True
            else:
                return False
        else:
            return False

    def set_color(self, r, g, b):
        set_color1 = Figure.__is_valid_color(self, r, g, b)
        if set_color1 is True:
            self.__color = r, g, b
        if set_color1 is False:
            pass

    def __is_valid_sides(self, *args):
        if args in float and int(*args) > 0:
            for valid in args:
                if valid > 0:
                    return True
                else:
                    return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = [*new_sides]
        elif len(new_sides) != self.sides_count:
            pass


class Circle(Figure):
    sides_count = 1

    def __init__(self, __sides, __color, filled=True):
        super().__init__(__sides, __color, filled)
        self.__radius = __sides

    def get_square(self):
        pass


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __sides, __color, filled):
        super().__init__(__sides, __color, filled)

    def get_square(self):
        pass


class Cube(Figure):
    sides_count = 12

    def __init__(self, __sides, __color, filled=True):
        super().__init__(__sides, __color, filled)
        self.__sides = 12

    def get_volume(self):
        return self.__sides


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
