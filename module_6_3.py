class Horse:
    def __init__(self, y_distance, x_distance=0, sound='Frrr'):
        super().__init__(self, y_distance, sound)
        self.x_distance = x_distance

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance = dy


class Pegasus(Horse, Eagle):
    def __init__(self, y_distance, x_distance, sound):
        super().__init__(y_distance, x_distance, sound)

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        pos = (self.x_distance, self.y_distance)
        return pos

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
