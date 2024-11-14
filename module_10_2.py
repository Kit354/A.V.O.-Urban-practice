import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def battle(self):
        enemy = 100
        start_time = time.time()
        while enemy:
            enemy -= self.power
            time.sleep(1)
            battle_time = time.time()
            day_battle_time = battle_time - start_time
            print(f'{self.name} сражается {day_battle_time: .0f} день(дня)..., осталось {enemy} воинов')
        finish_time = time.time()
        day = finish_time - start_time
        return day

    def run(self):
        print(f'{self.name}, на нас напали!')
        day = self.battle()
        print(f'{self.name} одержал победу спустя {day: .0f} дней')


first_knight = Knight('Sir Lancelot', 10)
first_knight.start()

second_knight = Knight("Sir Galahad", 20)
second_knight.start()
second_knight.join()
first_knight.join()
print('Все битвы закончились')
