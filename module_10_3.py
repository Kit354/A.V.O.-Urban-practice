import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            new_balance = random.randint(50, 500)
            if self.balance >= 500 and self.lock.locked() is True:
                self.lock.release()
            self.balance += new_balance
            print(f'Пополнение {new_balance}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            new_balance = random.randint(50, 500)
            print(f'Запрос на {new_balance}')
            if new_balance <= self.balance:
                self.balance -= new_balance
                print(f'Снятие: {new_balance}. Баланс: {self.balance}')
            elif new_balance > self.balance:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
